from mouse import Mouse
from keyboard_pc import Keyboard
from monitor import Monitor
from computer import Computer
from order import Order

teclado = Keyboard('HP', 'USB')
mouse = Mouse('HP', 'USB')
monitor = Monitor('LG', 'HDMI')
computadora = Computer('Personal', monitor, teclado, mouse)

teclado1 = Keyboard('HP', 'USB')
mouse1 = Mouse('HP', 'USB')
monitor1 = Monitor('Samsung', 'HDMI')
computadora1 = Computer('Office', monitor1, teclado1, mouse1)

teclado2 = Keyboard('Apple', 'Bluetooth')
mouse2 = Mouse('Apple', 'Bluetooth')
monitor2 = Monitor('Apple', 'HDMI')
computadora2 = Computer('Gamer', monitor2, teclado2, mouse2)

computers = [computadora, computadora1, computadora2]
order = Order(computers)
print(order.__str__())

order.add_computer(computadora)
print(order.__str__())