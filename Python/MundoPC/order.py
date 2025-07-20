class Order:
    order_counter = 0
    
    def __init__(self, computers):
        Order.order_counter += 1
        self.computers = computers
        self.id = Order.order_counter
    
    def add_computer(self, computer):
        self.computers.append(computer)

    def __str__(self):
        computers_str = ''
        for computer in self.computers:
            computers_str += '\n' + computer.__str__()
        return f'''Order: {self.id}
        {computers_str}'''