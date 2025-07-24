from input_dispositive import InputDispositive

class Monitor(InputDispositive):
    monitor_counter = 0

    def __init__(self, brand, input_type):
        Monitor.monitor_counter += 1
        self.id = Monitor.monitor_counter
        self.brand = brand
        self.input_type = input_type

    def __str__(self):
        return f'Monitor {{ Id: {self.id}, Marca: {self.brand}, Tipo de entrada: {self.input_type} }}'