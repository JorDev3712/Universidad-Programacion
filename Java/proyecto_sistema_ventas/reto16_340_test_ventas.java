package proyecto_sistema_ventas;

import proyecto_sistema_ventas.ventas.Orden;

class MainTestVentas {
    public static void main(String[] args) {
        System.out.println("*** Sales System ***");
        Orden order1 = new Orden();
        order1.addProducto("Soda", 3.5);
        order1.addProducto("Snacks", 4.0);
        order1.addProducto("Galleta", 1.0);
        order1.showOrder();

        Orden order2 = new Orden();
        order2.addProducto("Papas", 5.0);
        order2.addProducto("Hamburguesa", 15.0);
        order2.addProducto("Hotdog", 3.5);
        order2.showOrder();
    }
}
