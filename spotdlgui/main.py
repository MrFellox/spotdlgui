from kivy.app import App
from kivy.lang import Builder
from core.spotdlgui.scripts import utils as app_utils
from kivy.config import Config

# Disable option to exit the app when Esc is pressed.
Config.set('kivy', 'exit_on_escape', '0')

# Open app depending if it was maximized or not.
if app_utils.get_window_state() == True:
    Config.set('graphics', 'window_state', 'maximized')

from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.properties import BooleanProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from core.spotdlgui.scripts.popups import DownloadingPopup
from spotdl.download import DownloadManager
from spotdl.parsers.query_parser import parse_query
from spotdl.search import SpotifyClient
import os
import time
import ctypes
import threading

# Set high dpi

ctypes.windll.shcore.SetProcessDpiAwareness(1)

# Add fonts

KIVY_FONTS = [

    {
        'name': 'Gotham',
        'fn_regular': './core/spotdlgui/fonts/GothamBold.ttf'
    }

]

for font in KIVY_FONTS:
    LabelBase.register(**font)


# Initialize a Spotify client
# ! Client is initalized here to avoid any initalization error.
SpotifyClient.init(
    client_id="5f573c9620494bae87890c0f08a60293",
    client_secret="212476d9b0f3472eaa762d90b19b0ba8",
    user_auth=False
)


class Manager(ScreenManager):
    pass


class MainScreen(Screen):
    # Ran when settings button is clicked.
    def _enter_settings(self):
        '''
        This function runs when the "Settings" option is clicked,
        showing an animation to the settings screen.
        '''
        self.manager.current = 'optionsScreen'
        self.manager.transition.direction = 'left'

    def download_song(self):
        '''
        This function downloads the list of the song specified and shows progress of download in string.
        '''

        self.output_path = app_utils.get_download_path()

        # Get search query from the text entry
        # ! Replaced from App.get_running_app().ids['searcher'].text because we're now using screens.
        search_query = self.ids['searcher'].text

        self.popup.change_text('Searching song(s)...')

        # Parse songs
        self.song_list = parse_query(
            [search_query],
            'mp3',
            False,
            False,
            1
        )

        # Save app path

        app_path = os.path.dirname(os.path.realpath(__file__))

        # Move to the output path

        os.chdir(self.output_path)

        for song in self.song_list:
            # Change popup text

            self.popup.change_text(
                f'Attempting to download \n"{song.song_name}" by {song.contributing_artists[0]}...')

            with DownloadManager() as downloader:                
              downloader.download_single_song(song)
                    
            self.popup.change_text(
                f'Succesfully downloaded \n"{song.song_name}" to ' + self.output_path)
            time.sleep(3)

        # Clean text on entry

        self.ids['searcher'].text = ''

        # Move to the app path

        os.chdir(app_path)

        # Close popup
        self.popup.dismiss()

    def _on_download_press(self):
        '''
        Runs when donwload button is pressed
        '''
        # Start an instance of the progress popup and show it
        self.popup = DownloadingPopup()
        self.popup.open()

        # Start download thread.
        download_thread = threading.Thread(target=self.download_song)
        download_thread.start()


class OptionsScreen(Screen):
    # ! on_pre_enter is fired when the screen is about to be used: the entering animation is started.
    # ! so we use pre enter so it doesn't see the switches turn position by themselves.

    def on_pre_enter(self):
        # Update switch positions
        ask_location_switch = self.ids['askLocation_switch']
        ask_location_switch.active = app_utils.get_switch_setting(
            'askLocation')

    def switch_callback(self, instance, value):
        '''
        Runs everytime a switch that is linked to this callback is switched.
        '''
        if instance == 'askLocation':
            app_utils.change_config_value('askLocation', value)

        else:
            pass

    def change_default_path(self):
        output_path = app_utils.ask_for_default_path()
        app_utils.change_config_value('defaultLocation', output_path)

class SpotDLGUI(App):
    askLocation = BooleanProperty(app_utils.get_switch_setting('askLocation'))
    default_path = app_utils.default_path_kivy()

    def build(self):
        self.title = 'SpotDLGUI v1.1'

        # Event listeners
        Window.bind(on_maximize=self.on_maximize)
        Window.bind(on_restore=self.on_minimize)

        return Builder.load_file('core/spotdlgui/designs/ui.kv')

    # Kivy events
    def on_maximize(self, *args):
        try:
            app_utils.change_saved_window_state(True)

        except FileNotFoundError:
            pass

    def on_minimize(self, *args):
        try:
            app_utils.change_saved_window_state(False)

        except FileNotFoundError:
            pass


if __name__ == '__main__':
    SpotDLGUI().run()
