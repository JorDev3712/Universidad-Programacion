class Cliente:
    def __init__(self, id: int, name: str, last_name: str, membership: int):
        self.id = id
        self.name = name
        self.last_name = last_name
        self.membership = membership

    def __str__(self):
        return f'Id: {self.id}, Nombre: {self.name} {self.last_name}, Membresia: {self.membership}'
    
    def to_tuple(self)->tuple:
        return (self.id, self.name, self.last_name, self.membership)
        