package proyecto_sistema_ventas.ventas;

public class Orden {
    private Integer idOrder;
    private Integer counterProducts;
    public static Integer idCounter = 0;
    private Product[] products;

    private static final int MAX_PRODUCTS = 10;
    
    public Orden(){
        this.idOrder = ++Orden.idCounter;
        this.products = new Product[Orden.MAX_PRODUCTS];
        // this.products = new Product[]{
        //     new Product("Soda", 3.5),
        //     new Product("Snacks", 4.0),
        //     new Product("Galleta", 1.0)
        // };
        this.counterProducts = 0;
    }

    public Product[] getProducts() {
        return this.products;
    }

    public void addProducto(String nameProduct, Double costProduct){
        if (this.counterProducts >= Orden.MAX_PRODUCTS){
            System.out.println("Maximum product limit! " + Orden.MAX_PRODUCTS);
        }else{
            this.products[this.counterProducts++] = new Product(nameProduct, costProduct);
        }
    }
    
    public Double calculateTotal(){
        Double total = 0.0;
        for (var i = 0; i < this.products.length; i++){
            var product = this.products[i];
            if (product == null){
                continue;
            }
            total += product.getCost();
        }
        return total;
    }

    public void showOrder(){
        var totalOrder = this.calculateTotal();
        System.out.println(String.format("""
                Id Order: %d
                \tOrder Total: %f
                \tOrder Products:""", this.idOrder, totalOrder));
        for (var i = 0; i < this.products.length; i++){
            var product = this.products[i];
            if (product == null){
                continue;
            }
            System.out.println("\t\t" + product.toString());
        }
    }

}
