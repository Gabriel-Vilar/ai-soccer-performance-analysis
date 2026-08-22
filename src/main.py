class Player():
    def __init__(self, name: str, age: int, position: str):
        self.name = name
        self.age = age
        self.position = position
    def __repr__(self):
        return (f'Name: {self.name}\n'
                f'Age: {self.age}\n'
                f'Position: {self.position}')

p1 = Player("Gabriel Vilar", 18, "Attacking Midfielder")
print(p1)

