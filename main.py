from core.spotdlgui.scripts import utils as app_utils
from kivy.app import App
from kivy.config import Config
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.text import LabelBase

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

class SpotDLApp(App):
    def build(self):
        self.title = 'SpotDLGUI v1.0'
        return Builder.load_file('core/designs/ui.kv')


if __name__ == '__main__':
    SpotDLApp().run()
