from mouse import Mouse
from keyboard_pc import Keyboard
from monitor import Monitor

class Computer:
    computer_counter = 0

    def __init__(self, name, monitor, keyboard, mouse):
        self.name = name
        self.monitor = monitor
        self.keyboard = keyboard
        self.mouse = mouse

    def __str__(self):
        return (f'''Computadora: {self.name}
        {self.monitor},
        {self.keyboard},
        {self.mouse}''')

# main code
if __name__ == '__main__':
    teclado = Keyboard('HP', 'USB')
    mouse = Mouse('HP', 'USB')
    monitor = Monitor('LG', 'HDMI')
    computadora = Computer('HP', monitor, teclado, mouse)

    print(computadora)
