package proyecto_sistema_ventas.ventas;

public class Product {
    private Integer idProduct;
    private String name;
    private Double cost;

    public static Integer idCounter = 0;

    public Product(String name, Double cost){
        this.idProduct = ++Product.idCounter;
        this.name = name;
        this.cost = cost;
    }

    public Integer getIdProduct() {
        return this.idProduct;
    }

    public String getName() {
        return this.name;
    }

    public Double getCost() {
        return this.cost;
    }

    @Override
    public String toString() {
        return "Product {idProduct=" + idProduct + ", name=" + name + ", cost=" + cost + "}";
    }
}
