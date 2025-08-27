import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror
from services.clienteService import ClienteService
from models.cliente import Cliente

class ZonaFitWindow(tk.Tk):
    def __init__(self, clienteService: ClienteService):
        super().__init__()
        self.clienteService = clienteService
        self.config_window()
        self.config_style()
        self.config_grid()
        self.create_title()
        self.create_form()
        self.create_table()
        self.create_buttons()
        self.load_table_data()
        self.config_events()
        # This global variable will store the selected item from the table
        self.element_selected = ''

    def config_window(self):
        # Sets size the window
        self.geometry('900x600')
        # No Resize the window
        self.resizable(0,0)
        # Changes the window color
        self.configure(background='#1d2d44')
        # Edits the title
        self.title('Zona Fit App')

    def config_style(self):
        # We define a style
        self.estilos = ttk.Style()
        self.estilos.theme_use('clam') # Dark theme
        self.estilos.configure(self, background='#1d2d44',
                 foreground='white',
                 fieldbackground='black')
        self.estilos.configure('Treeview', background='black',
                        foreground='white',
                        fieldbackground='black',
                        rowheight=30)
        self.estilos.configure('TButton', background='#3a86ff',
                               foreground='white', 
                               height=45, 
                               width=20)

        self.estilos.map('Treeview', background=[('selected', '#3a86ff')])
        self.estilos.map('Treeview.Heading', background=[('active', '#1d2d44')])
        self.estilos.map('TButton', background=[('hover', '#1d2d44')])

    def config_grid(self):
        # We configure the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=2)
        self.rowconfigure(2, weight=1)

    def create_title(self):
        # title to frame
        label = ttk.Label(self, text='Zona fit (GYM)', font=('Arial', 20))
        label.grid(row=0, column=0, columnspan=2)

    def create_form(self):
        frame = ttk.Frame(self)
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=3)

        name_label = ttk.Label(frame, text='Nombre: ', font=('Arial', 12))
        name_label.grid(row=0, column=0, sticky=tk.W, padx=20, pady=50)

        self.name_textBox = ttk.Entry(frame, font=('Arial', 12))
        self.name_textBox.grid(row=0, column=1, sticky=tk.EW, padx=5, pady=50)

        lastname_label = ttk.Label(frame, text='Apellido:', font=('Arial', 12))
        lastname_label.grid(row=1, column=0, sticky=tk.W, padx=20, pady=5)

        self.lastname_textBox = ttk.Entry(frame, font=('Arial', 12))
        self.lastname_textBox.grid(row=1, column=1, sticky=tk.EW, padx=5, pady=5)

        membership_label = ttk.Label(frame, text='Membresia: ', font=('Arial', 12))
        membership_label.grid(row=2, column=0, sticky=tk.W, padx=20, pady=50)

        self.membership_textBox = ttk.Entry(frame, font=('Arial', 12))
        self.membership_textBox.grid(row=2, column=1, sticky=tk.EW, padx=5, pady=50)

        frame.grid(row=1, column=0, sticky=tk.NSEW)

    def create_table(self):
        frame = ttk.Frame(self)
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=0)

        # We define the columns
        columnas = ('Id', 'Nombre', 'Apellido', 'Membresia')
        self.table = ttk.Treeview(frame, columns=columnas, show='headings')

        # Table header
        self.table.heading('Id', text='Id', anchor=tk.CENTER)
        self.table.heading('Nombre', text='Nombre', anchor=tk.W)
        self.table.heading('Apellido', text='Apellido', anchor=tk.W)
        self.table.heading('Membresia', text='Membresia', anchor=tk.CENTER)

        # Column format
        self.table.column('Id', width=5, anchor=tk.CENTER)
        self.table.column('Nombre', width=100, anchor=tk.W)
        self.table.column('Apellido', width=100, anchor=tk.W)
        self.table.column('Membresia', width=40, anchor=tk.CENTER)

        self.table.grid(row=0, column=0, sticky=tk.NSEW)

        # We add a scrollbar
        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.table.yview)
        self.table.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky=tk.NS)

        frame.grid(row=1, column=1, padx=20, sticky=tk.NSEW)

    def clear_fields(self):
        self.name_textBox.delete('0', tk.END)
        self.name_textBox.insert('0', '')

        self.lastname_textBox.delete('0', tk.END)
        self.lastname_textBox.insert('0', '')

        self.membership_textBox.delete('0', tk.END)
        self.membership_textBox.insert('0', '')

    def clear_table(self):
        self.table.delete(*self.table.get_children())

    def load_table_data(self):
        self.clear_table()
        clients = self.clienteService.getClients()
        for client in clients:
            self.table.insert(parent='', index=tk.END, values=client.to_tuple())
        self.lastId = self.clienteService.get_auto_increment_of_client_table() - 1
        print(f'Last Id of table db Clientes={self.lastId + 1}')

    def validate_int(self, value: str)->bool:
        try:
            int(value)
            return True
        except:
            return False

    def on_save_button_click(self, event):
        name = self.name_textBox.get()
        if name == '':
            showerror(title='Error!', message='Por favor, ingresa un nombre.')
            return
        lastname = self.lastname_textBox.get()
        if lastname == '':
            showerror(title='Error!', message='Por favor, ingresa un apellido.')
            return
        membership = self.membership_textBox.get()
        if self.validate_int(membership) is False:
            showerror(title='Error!', message='Por favor, ingresa un valor númerico en la membresia.')
            return
        
        # Updates a item from the table and db
        if self.element_selected != '':
            element = self.table.item(self.element_selected) # item
            if element is not None:
                client = Cliente(element['values'][0], name, lastname, int(membership))
                result = self.clienteService.updateClient(client)
                # Method to update a item
                self.table.item(self.element_selected, values=client.to_tuple())
                showinfo('Guardar', 'Se actualizaron los datos del cliente.')
                self.clear_fields()
                self.element_selected = ''

        else:
            # Adds a item to table and db
            result = self.clienteService.addClient(name, lastname, membership)
            if result:
                self.lastId = self.lastId + 1
                self.table.insert(parent='', index=tk.END, values=(self.lastId, name, lastname, int(membership)))
                showinfo('Guardar', 'Se agregó un nuevo cliente.')
                self.clear_fields()

    def on_delete_button_click(self, event):
        if self.element_selected != '':
            element = self.table.item(self.element_selected) # item
            if element is not None:
                row = element['values']
                client = Cliente(row[0], row[1], row[2], int(row[3]))
                result = self.clienteService.deleteClient(client)
                if result:
                    self.table.delete(self.element_selected)
                    showinfo('Eliminar!', message='Se ha eliminado el cliente.')
                    self.clear_fields()
                    self.element_selected = ''


    def on_clear_button_click(self, event):
        self.clear_fields()
        self.table.selection_remove(self.element_selected)
        self.element_selected = ''

    def create_buttons(self):
        frame = ttk.Frame(self)
        frame.columnconfigure(0, weight=2)
        frame.columnconfigure(1, weight=1)
        frame.columnconfigure(2, weight=2)

        self.save_button = ttk.Button(frame, text='Save')
        self.save_button.grid(row=0, column=0, padx=30)

        self.delete_button = ttk.Button(frame, text='Delete')
        self.delete_button.grid(row=0, column=1, padx=30)

        self.clear_button = ttk.Button(frame, text='Clear')
        self.clear_button.grid(row=0, column=2, padx=30)
        
        frame.grid(row=2, column=0, columnspan=2, sticky=tk.NS)

    def config_events(self):
        # Associates the "select" event of the table
        self.table.bind('<<TreeviewSelect>>', self.show_selected)
        self.save_button.bind('<Button-1>', self.on_save_button_click) # Mouse Left Click
        self.delete_button.bind('<Button-1>', self.on_delete_button_click)  # Mouse Left Click
        self.clear_button.bind('<Button-1>', self.on_clear_button_click) # Mouse Left Click

    # Shows selected row
    def show_selected(self, event):
        print('On show_selected()')
        selection = self.table.selection()
        if len(selection) == 0:
            print("No hay elementos seleccionados")
            return

        self.element_selected = selection[0] # item str
        element = self.table.item(self.element_selected) # item
        if element is not None:
            row = element['values']
            self.name_textBox.delete('0', 'end')
            self.name_textBox.insert('0', row[1])

            self.lastname_textBox.delete('0', 'end')
            self.lastname_textBox.insert('0', row[2])

            self.membership_textBox.delete('0', 'end')
            self.membership_textBox.insert('0', row[3])