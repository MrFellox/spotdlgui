from kivy.core import text
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

    def change_text(self, text):
        self.change_label_size(len(text))
        self.ids.popup_label.text = text

    def change_label_size(self, text_len: int):
        '''
        Changes the size of the label so it fits on the popup.
        '''

        self.ids.popup_label.font_size = (self.width / text_len) + 10