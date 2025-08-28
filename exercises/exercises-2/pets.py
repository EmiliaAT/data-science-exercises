class Pet:
    def __init__(self, name: str, species: str):
        self.name = name
        self.species = species


    def __repr__(self) -> str:
        return f'Pet {self.name} is a {self.species}'


    def display(self):
        print(self)