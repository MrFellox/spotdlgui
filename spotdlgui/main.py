from spotdl import download
from core.spotdlgui.scripts import utils as app_utils
from kivy.app import App
from kivy.config import Config
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.text import LabelBase
from core.spotdlgui.popups import DownloadingPopup
from spotdl.download import DownloadManager
from spotdl.parsers.query_parser import parse_query
from spotdl.search import SpotifyClient
import threading
import os

# Disable option to exit the app when Esc is pressed.
Config.set('kivy', 'exit_on_escape', '0')

# Open app depending if it was maximized or not.
if app_utils.get_window_state() == True:
    Config.set('graphics', 'window_state', 'maximized')
else:
    Config.set('graphics', 'width', '800')
    Config.set('graphics', 'height', '500')


# Add fonts

KIVY_FONTS = [

    {
        'name': 'Gotham',
        'fn_regular': './core/spotdlgui/fonts/GothamBold.ttf'
    }
    
]

for font in KIVY_FONTS:
    LabelBase.register(**font)

class SpotDLGUI(App):
    def build(self):
        self.title = 'SpotDLGUI v1.0'

        # Initialize a Spotify Client

        SpotifyClient.init(
            client_id="5f573c9620494bae87890c0f08a60293",
            client_secret="212476d9b0f3472eaa762d90b19b0ba8",
            user_auth=False
        )

        return Builder.load_file('core/designs/ui.kv')

    def download_song(self):
        # Get url from the text entry
        url = App.get_running_app().root.ids['url_entry'].text

        # Get Desktop path
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

        song_list = parse_query(
            [url],
            'mp3',
            False,
            False,
            1
            )
       
        # Save current directory.
        
        app_path = os.path.dirname(os.path.realpath(__file__))

        # Move to desktop to save songs there
        os.chdir(desktop)

        # Download

        with DownloadManager() as downloader:
            downloader.download_multiple_songs(song_list)
        # Move to the app path

        os.chdir(app_path)

        # Close popup
        self.popup.dismiss()

    def _on_download_press(self):
        # Show popup

        self.popup = DownloadingPopup()
        self.popup.open()

        Clock.schedule_once(self._start_download_thread)

    def _start_download_thread(self, instance):
        self.thread = threading.Thread(target=self.download_song)
        self.thread.start()

if __name__ == '__main__':
    SpotDLGUI().run()