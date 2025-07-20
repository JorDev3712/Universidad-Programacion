from input_dispositive import InputDispositive

class Keyboard(InputDispositive):
    keyboard_counter = 0

    def __init__(self, brand, input_type):
        Keyboard.keyboard_counter += 1
        self.id = Keyboard.keyboard_counter
        self.brand = brand
        self.input_type = input_type

    def __str__(self):
        return f'Teclado {{ Id: {self.id}, Marca: {self.brand}, Tipo de entrada: {self.input_type} }}'