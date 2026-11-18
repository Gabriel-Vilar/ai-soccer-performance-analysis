import json
from pathlib import Path

from src.models import Player


def save_players(list_, filename):
    filename = Path(filename)
    filename.parent.mkdir(parents=True, exist_ok=True)
    list2 = [player.to_dict() for player in list_]
    with open(filename, 'w', encoding='utf8') as file_:
        json.dump(list2, file_, ensure_ascii=False, indent=2)


def load_players(filename):
    try:
        with open(filename, 'r', encoding='utf8') as file_:
            dict_players = json.load(file_)
            list2 = [Player(player['Name'], player['Age'], player['Position'])
                     for player in dict_players]
            return list2
    except FileNotFoundError:
        print(f'The file ({filename}) was not found. Starting with an empty list')
        return []
    except json.JSONDecodeError:
        print('File exists but the json format is corrupted')
        raise