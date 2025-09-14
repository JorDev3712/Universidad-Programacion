package proyecto_maquina_snacks.classes;

import java.util.ArrayList;
import java.util.List;

public class SnackManager {
    private static final List<Snack> snacks;

    static{
        snacks = new ArrayList<>();
        snacks.add(new Snack("Papas", 70.0));
        snacks.add(new Snack("Refresco", 50.0));
        snacks.add(new Snack("Sandwich", 120.0));
    }

    public static void addSnack(Snack snack){
        snacks.add(snack);
    }

    public static void showSnacks(){
        System.out.println("--- Snacks in Inventory ---");
        for (Snack snack : getSnacks()) {
            System.out.println(snack.toString());
        }
    }

    public static List<Snack> getSnacks() {
        return snacks;
    }
}
