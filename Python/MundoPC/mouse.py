from input_dispositive import InputDispositive

class Mouse(InputDispositive):
    mouse_counter = 0

    def __init__(self, brand, input_type):
        Mouse.mouse_counter += 1
        self.id = Mouse.mouse_counter
        self.brand = brand
        self.input_type = input_type

    def __str__(self):
        return f'Mouse {{ Id: {self.id}, Marca: {self.brand}, Tipo de entrada: {self.input_type} }}'