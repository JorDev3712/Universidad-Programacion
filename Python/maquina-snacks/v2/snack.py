class Snack:
    snacks_counter = 0

    # Defining Properties No Repeat
    def __init__(self, name: str, cost):
        Snack.snacks_counter += 1
        self.id = Snack.snacks_counter
        self.name = name
        self.cost = cost
    
    def __str__(self):
        return f'Id: {self.id}, Nombre: {self.name}, Precio: {self.cost}'