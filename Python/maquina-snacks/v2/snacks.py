from snack import Snack

class Snacks:
    
    # Defining Properties No Repeat
    def __init__(self):
        self.list_snacks = [Snack('Papas', 2.5),
                            Snack('Gaseosa', 3.00),
                            Snack('Sandwich', 8.9)]

    # Add new snack
    def add_snack(self, snack: Snack):
        self.list_snacks.append(snack)

    def __str__(self):
        str_extend = ''
        for snack in self.list_snacks:
            str_extend += f'\t{snack.__str__()}' + '\n'
        return str_extend