package proyecto_maquina_snacks.v2.services;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;

import proyecto_maquina_snacks.v2.dominion.Snack;

public class ServicioSnacks implements IServicioSnacks {
    public final String FILE_NAME = "snacks.txt";
    private List<Snack> snacks;

    @Override
    public Snack getSnack(Integer id){
        for (Snack snack : this.snacks){
            if (snack.getIdSnack() == id){
                return snack;
            }
        }
        return null;
    }

    @Override
    public void initialize(){
        this.snacks = new ArrayList<>();
        var file = new File(this.FILE_NAME);
        try {
            if (file.exists()) {
                System.out.println("File already exists!");
                this.snacks = this.getSnacks();
            } else {
                //Creamos el archivo
                var salida = new PrintWriter(new FileWriter(file));
                this.snacks.add(new Snack("Papas", 70.0));
                this.snacks.add(new Snack("Refresco", 50.0));
                this.snacks.add(new Snack("Sandwich", 120.0));
                for (Snack snack : this.snacks){
                    salida.println(snack.toFile());
                }
                // Se guarda el archivo a disco duro
                salida.close();
                System.out.println("Se ha creado el archivo");
            }
        } catch(IOException e){
            System.out.println("Error al crear archivo: " + e.getMessage());
            e.printStackTrace();
        }
    }


    @Override
    public void addSnack(String name, Double cost) {
        boolean anexar = false;
        var file = new File(this.FILE_NAME);
        try{
            anexar = file.exists();
            var salida = new PrintWriter(new FileWriter(file, anexar));
            var snack = new Snack(name, cost);
            this.snacks.add(snack);
            salida.println(snack.toFile());
            salida.close();
        }catch (IOException e){
            System.out.println("Error al crear archivo: " + e.getMessage());
            e.printStackTrace();
        }
    }

    @Override
    public void showSnacks() {
        System.out.println("--- Snacks in Inventory ---");
        for (Snack snack : getSnacks()) {
            System.out.println(snack.toString());
            // This allows that the snack id counter to be different
            Snack.snackCounter = snack.getIdSnack();
        }
    }

    @Override
    public List<Snack> getSnacks() {
        var snacks = new ArrayList<Snack>();
        var file = new File(this.FILE_NAME);
        try{
            System.out.println("Reading file contents....");
            // Abrir el archivo para lectura
            var entrada = new BufferedReader(new FileReader(file));
            // Leemos linea a linea el archivo
            var lineRead = "";
            // Leemos todas las lineas
            while(lineRead != null){
                System.out.println(lineRead);
                // antes de terminar el ciclo, nos movemos a la siguiente linea
                lineRead = entrada.readLine();
                if (lineRead == null){
                    break;
                }

                var lineSplit = lineRead.split(",");
                snacks.add(new Snack(Integer.parseInt(lineSplit[0]), lineSplit[1], Double.parseDouble(lineSplit[2]) ));
            }
            // Cerrar archivo
            entrada.close();
        }catch(Exception e){
            System.out.println("Error al leer archivo: " + e);
        }
        return snacks;
    }
}
