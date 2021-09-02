from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.core.text import LabelBase

KIVY_FONTS = [

    {
        'name': 'Gotham',
        'fn_regular': './core/spotdlgui/fonts/GothamBold.ttf'
    }
    
]

for font in KIVY_FONTS:
    LabelBase.register(**font)

class DownloadingPopup(Popup):
    def __init__(self):
        super(DownloadingPopup, self).__init__()

        self.title = 'Downloading...'
        self.ids.popup_label.text = f'Attempting to download song(s).'