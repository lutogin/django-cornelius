from os import path
import json

BASE_DIR = path.dirname(path.dirname(path.abspath(__file__)))
CONFIG_PATH = path.join(BASE_DIR, 'app', 'config', 'config.json')


def get_config():
    with open(CONFIG_PATH, 'r') as conf:
        configs = json.load(conf)

    return configs
