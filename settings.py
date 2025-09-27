import os
import json

SETTINGS_FILE = 'userSettings.json'

default_settings = {
    "name" : "Friend",
    "bedtime" : "23:00", 
    "waketime" : "08:00",
    "walkingSpeed" : 5,  # km/h
    "locationPermission" : True
}

def load_settings():  # Load settings from file or return default settings
    if not os.path.exists(SETTINGS_FILE):
        return default_settings

    with open(file_path, 'r') as file:
        settings = json.load(file)

    return settings


def save_settings(settings):  # save settings to file
    with open(SETTINGS_FILE, 'w') as file:
        json.dump(settings, file, indent=4)

def update_setting(key, value):  # update individual setting
    settings = load_settings()
    settings[key] = value
    save_settings(settings)    

def get_single_setting(key):  # retrieve individual setting
    settings = load_settings()
    return settings.get(key, default_settings.get(key))
