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

def get_arguments(queries: list, desktop_path: str) -> dict:
    '''
    Sets arguments that DowloadManager needs.
    (Default arguments were taken from SpotDL code.)
    '''

    with open('core/spotdlgui/args.json') as f:
        args = json.load(f)

    # Add the queries

    args['query'] = queries
    args['output'] = desktop_path

    return args
