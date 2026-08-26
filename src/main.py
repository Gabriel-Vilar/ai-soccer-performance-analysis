playerlist = []
class Player():
    def __init__(self, name: str, age: int, position: str):
        self.name = name
        self.age = age
        self.position = position
    def __repr__(self):
        return (f'Name: {self.name}\n'
                f'Age: {self.age}\n'
                f'Position: {self.position}\n')

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



p1 = Player('Gabriel Vilar', 18, 'Attacking Midfielder')
p2 = Player('Matheus Vilar', 18, 'Left Winger')
p3 = Player('Cristiano Ronaldo', 41, 'Stricker')
p4 = Player('Lionel Messi', 39, 'Right Winger')
p5 = Player('Neymar Jr', 34, 'Attacking Midfielder')

addplayer(playerlist, p1, p2, p3, p4, p5)
showplayers(playerlist)
findplayer(playerlist, 'vilar')




