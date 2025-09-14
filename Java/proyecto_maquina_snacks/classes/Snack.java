package proyecto_maquina_snacks.classes;

public class Snack {
    public static Integer snackCounter = 0;

    private Integer idSnack;
    private String name;
    private Double cost;

    public Snack(String name, Double cost){
        this.idSnack = ++Snack.snackCounter;
        this.name = name;
        this.cost = cost;
    }

    public Integer getIdSnack() {
        return idSnack;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Double getCost() {
        return cost;
    }

    public void setCost(Double cost) {
        this.cost = cost;
    }

    @Override
    public int hashCode() {
        final int prime = 31;
        int result = 1;
        result = prime * result + ((this.idSnack == null) ? 0 : this.idSnack.hashCode());
        result = prime * result + ((this.name == null) ? 0 : this.name.hashCode());
        result = prime * result + ((this.cost == null) ? 0 : this.cost.hashCode());
        return result;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj)
            return true;
        if (obj == null)
            return false;
        if (getClass() != obj.getClass())
            return false;
        Snack other = (Snack) obj;
        if (this.idSnack == null) {
            if (other.idSnack != null)
                return false;
        } else if (!this.idSnack.equals(other.idSnack))
            return false;
        if (this.name == null) {
            if (other.name != null)
                return false;
        } else if (!this.name.equals(other.name))
            return false;
        if (this.cost == null) {
            if (other.cost != null)
                return false;
        } else if (!this.cost.equals(other.cost))
            return false;
        return true;
    }

    @Override
    public String toString() {
        return "Snack [idSnack=" + this.idSnack + ", name=" + this.name + ", cost=" + this.cost + "]";
    }
}
