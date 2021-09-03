import json

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

    # ! Revamp error handling and make so it writes default configurations, when options are introduced.
    # Error while trying to read file, possibly changed by user.    
    except Exception as e:
        print(e)

        try:
            with open('./core/data/config.json', 'w') as f:
                settings = json.load(f)

                settings['isMaximized'] == False

                json.dump(settings, f, indent = 2)

        except Exception as e:
            print('An error ocurred while trying to fix isMaximized value.')
            print(e)

            # Fix to default value

            default_data = {"isMaximized": False}

            with open('./core/data/config.json', 'w') as f:
                json.dump(default_data, f, indent=2)

def change_saved_window_state(state: bool):
    # Open config file
    with open ('./core/data/config.json') as f:
        configs = json.load(f)

    configs['isMaximized'] = state

    with open ('./core/data/config.json', 'w') as f:
        json.dump(configs, f, indent=2)
