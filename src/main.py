from pathlib import Path
import json

playerlist = []
FILE_NAME = Path().parent / 'data'/ 'players.json'

class Player():
    def __init__(self, name: str, age: int, position: str):
        self.name = name
        self.position = position
        self.age = age

    def __repr__(self):
        return (f'Name: {self.name}\n'
                f'Age: {self.age}\n'
                f'Position: {self.position}\n')

    def __eq__(self, other):
        if not isinstance(other, Player):
            return NotImplemented

        return self.name.lower() == other.name.lower()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name2):
        if not isinstance(name2, str) or not name2.strip():
            raise ValueError('Invalid name, the player could not be created.')
        self._name = name2
        
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 16:
            raise ValueError('Invalid age, the following player could not be created:\n'
            f'Name: {self.name}\n'
            f'Age: {value}\n'
            f'Position: {self.position}\n')
        self._age = value

    def to_dict(self): 
        return {
        'Name': self.name,
        'Age': self.age,
        'Position': self.position
    }
    

def showplayers(list_: list):
    for player in list_:
        print(player)


def addplayer(list_: list, *args):
    list_.extend(args)

def findplayer(list_: list, name: str):
    found = [player for player in list_ if name.lower() in player.name.lower()]
    if not found:
        print('PLayer not found')
        return
    if len(found) > 1:
         print(f'Players found({len(found)}):\n')
    else: 
        print(f'Player found:')
    for player in found:
        print(player)

def removeplayer(list_, *args):
    targets = [name.lower() for name in args]
    list_[:] = [
        player for player in list_ 
        if not any(target in player.name.lower() for target in targets)
    ]

def save_players(list_, filename):
    filename = Path(filename)
    filename.parent.mkdir(parents=True, exist_ok=True)
    list2 = [player.to_dict() for player in list_]
    with open(filename, 'w', encoding = 'utf8') as file_:
        json.dump(list2, file_, ensure_ascii = False, indent=2 )
        
def load_players(filename):
    try:
        with open(filename, 'r', encoding = 'utf8') as file_:
            dict_players = json.load(file_)
            list2= [Player(player['Name'], player['Age'], player['Position']) for player in dict_players]
            return list2
    except FileNotFoundError:
        print(f'The file ({filename}) was not found. Starting with an empty list')
        return []
    except json.JSONDecodeError:
        print('File exists but the json format is corrupted')
        raise



if __name__ == '__main__':
    p1 = Player('Gabriel Vilar', 18, 'Attacking Midfielder')
    p2 = Player('Gabriel Vilar', 18, 'Left Winger')
    p3 = Player('Cristiano Ronaldo', 41, 'Stricker')
    p4 = Player('Lionel Messi', 39, 'Right Winger')
    p5 = Player('Neymar Jr', 34, 'Attacking Midfielder')

    addplayer(playerlist, p1, p2, p3, p4, p5)
    showplayers(playerlist)
    findplayer(playerlist, 'vilar')
    removeplayer(playerlist, 'vilar')
    showplayers(playerlist)
    print(p1 == p2)
    p1_dicted = p1.to_dict()
    save_players(playerlist, FILE_NAME)
    print()
    loaded_players = load_players(FILE_NAME)
    




