import json
default_settings = {"isMaximized": False}

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
