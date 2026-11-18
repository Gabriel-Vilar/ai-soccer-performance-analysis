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
        print('Player not found')
        return
    if len(found) > 1:
        print(f'Players found({len(found)}):\n')
    else:
        print('Player found:')
    for player in found:
        print(player)


def removeplayer(list_, *args):
    targets = [name.lower() for name in args]
    list_[:] = [
        player for player in list_
        if not any(target in player.name.lower() for target in targets)
    ]