from flask import Flask, redirect, url_for
from flask import render_template
from db.conexion import ConnectionMysql
from services.clienteService import ClienteService
from models.cliente import Cliente
from repository.client_form import ClientForm

app = Flask(__name__)
conn = ConnectionMysql('reto_mysql_db1', 'root', '')
service = ClienteService(conn)

titulo_app = 'Zona Fit (GYM)'

app.config['SECRET_KEY'] = 'llave_secreta'

@app.route('/') # url: http://localhost:5000/
@app.route('/index.html') # url: http://localhost:5000/index.html
def inicio():
    app.logger.debug('Inicio de página.')
    # We obtain the clients from the db
    clients_db = service.getClients()

    # We make a empty client object
    client = Cliente(None, None, None, 0)
    client_form = ClientForm(obj=client)

    return render_template('index.html', titulo=titulo_app, clients=clients_db, forma=client_form)

@app.route('/save', methods=['POST'])
def save():
    # We make the empty objets of client
    client = Cliente(None, None, None, 0)
    client_form = ClientForm(obj=client)
    if client_form.validate_on_submit():
        # We init the client object with the values from the form
        client_form.populate_obj(client)
        if not client.id:
            # We save the new client into db
            result = service.addClient(client.name, client.last_name, client.membership)
            if result:
                app.logger.debug('New client added!')
        else:
            result = service.updateClient(client)
            if result:
                app.logger.debug('New client updated!')
        # We redirect to the home page
        return redirect(url_for('inicio'))
    
@app.route('/edit/<int:id>') # localhost:5000/editar/1
def edit(id: int):
    client = service.getCliente(id)
    if client is None:
        return redirect(url_for('inicio'))
    client_form = ClientForm(obj=client)
    clients_db = service.getClients()
    # Volvemos a enviar los parámetros porque el protocolo HTTP no tiene memoria y en cada petición se pierden los datos.
    return render_template('index.html', titulo=titulo_app, clients=clients_db, forma=client_form)

@app.route('/delete/<int:id>') # localhost:5000/delete/1
def delete(id: int):
    client = service.getCliente(id)
    if client is None:
        return redirect(url_for('inicio'))
    result = service.deleteClient(client)
    if result:
        app.logger.debug(f'Client id={client.id} has deleted!')
    # We redirect to the home page
    return redirect(url_for('inicio'))

@app.route('/clear')
def clear():
    # We redirect to the home page
    return redirect(url_for('inicio'))

if __name__ == '__main__':
    app.run(debug=True)