import os
import json

_default_prefs = {
    'slicing': [
        'manchego',
        'sharp cheddar'
    ],
    'spreadable': [
        'Saint Andre',
        'camembert',
        'bucheron',
        'goat',
        'humbilt fog',
        'cambozola'
    ],
    'salads': [
        'crumbled feta'
    ]
}


def read_cheese_preferences():
    full_path = os.path.expanduser('~/.cheese.json')
    with open(full_path, 'r') as f:
        prefs = json.load(f)
        return prefs


def write_cheese_preferences(prefs):
    full_path = os.path.expanduser('~/.cheese.json')
    with open(full_path, 'w') as f:
        json.dump(prefs, f, indent=4)


def write_default_cheese_preferences():
    write_cheese_preferences(_default_prefs)
