import json
import os
import tkinter as tk
from tkinter import filedialog

default_settings = {"isMaximized": False, "askLocation": True, 'defaultLocation': None}

def get_window_state() -> bool:
    '''
    Returns True or False if the last app instance was maximized or not.
    '''

    try:
        with open('./core/data/config.json') as f:
            settings = json.load(f)

            if settings['isMaximized'] == False or settings['isMaximized'] == True:
                return settings['isMaximized']

            else:
                settings['isMaximized'] = False
                with open('./core/data/config.json', 'w') as f:
                    json.dump(settings, f, indent=2)

    # ! Revamp error handling and make so it writes default configurations, when options are introduced.
    # Error while trying to read file, possibly changed by user.   
    except Exception as e:
        print('Error while reading window state:')
        print(e)
        create_config_file()
        return False
        
def change_saved_window_state(state: bool):
    # Open config file
    with open ('./core/data/config.json') as f:
        configs = json.load(f)

    configs['isMaximized'] = state

    with open ('./core/data/config.json', 'w') as f:
        json.dump(configs, f, indent=2)

def create_config_file():
    '''
    Creates/overwrites the config file with the default settings.
    '''
    os.mkdir('./core/data')
    with open('./core/data/config.json' 'w') as f:
        json.dump(default_settings, f, indent=2)
        
def get_switch_setting(setting):
    '''
    'Gets the value of the config.json of the specified setting and returns the correct value for Kivy
    '''
    with open('./core/data/config.json') as f:
        data = json.load(f)

    return data[setting]

def change_config_value(setting, value):
    '''
    Modifies the specified setting for the specified value 
    '''
    
    with open('./core/data/config.json') as f:
        data = json.load(f)

        data[setting] = value

    with open('./core/data/config.json', 'w') as f:
        json.dump(data, f, indent=2)

def get_setting_value(setting):
    '''
    Returns the value of the specified setting
    '''
    with open('./core/data/config.json') as f:
        data = json.load(f)

    return data[setting]

def get_download_path() -> str:
    '''
    Returns the path to the selected folder where the user wants to save songs.
    '''
    if get_setting_value('askLocation') == True:
        output = ''

        # Using tk since it uses system's ui.
        root = tk.Tk()
        root.withdraw()
        
        while output == '':
            output = filedialog.askdirectory()
        
    else:
        # Get Desktop path
        output = os.path.join(os.path.join(
            os.environ['USERPROFILE']), 'Desktop')

    return output
