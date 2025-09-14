package proyecto_maquina_snacks;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

import proyecto_maquina_snacks.classes.Snack;
import proyecto_maquina_snacks.classes.SnackManager;

class MainSnackMachine {
    public static void main(String[] args) {
        snackMachine();
    }

    public static void snackMachine(){
        System.out.println("*** Snack Machine ***");

        // We save client productos
        List<Snack> products = new ArrayList<>();
        SnackManager.showSnacks();
        System.out.println();

        var sc = new Scanner(System.in);
        var exit = false;
        while (!exit) {
            showMenu();
            var option = Integer.parseInt(sc.nextLine());
            exit = executeOptions(sc, option, products);
        }
        sc.close();
    }

    private static void showMenu(){
        System.out.print("""
                Menu:
                1. Buy Snack.
                2. Show Ticket.
                3. Add a new Snack.
                4. Exit.
                Choose an option:\s""");
    }

    private static Boolean executeOptions(Scanner sc, int menuOption, List<Snack> clientProductos){
        var exit = false;
        switch (menuOption) {
            case 1 -> buySnack(sc, clientProductos);
            case 2 -> showTicket(clientProductos);
            case 3 -> addSnack(sc);
            case 4 -> {
                System.out.println("Closing machine... See you soon!");
                exit = true;
            }
            default -> System.out.println("Invalid option...");
        }
        return exit;
    }

    private static void buySnack(Scanner sc, List<Snack> clientProductos){
        System.out.print("What snack do you want to buy? (id): ");
        var snackId = Integer.parseInt(sc.nextLine());
        var found = false;
        for (Snack snack : SnackManager.getSnacks()){
            if (snack.getIdSnack() == snackId){
                clientProductos.add(snack);
                System.out.println("Ok, Snack added: " + snack.toString());
                found = true;
                break;
            }
        }

        if (!found){
            System.out.println("No snack was found with the id=" + snackId);
        }
    }

    private static void showTicket(List<Snack> clientProductos){
        System.out.println("*** Selling Ticket ***");
        var total = 0;
        for (Snack snack : clientProductos){
            System.out.println(String.format("\t- %s - $%f", snack.getName(), snack.getCost()));
            total += snack.getCost();
        }
        System.out.println("\tTotal: $" + total);
    }

    private static void addSnack(Scanner sc){
        System.out.println("*** Create a Snack ***");
        System.out.print("Snack name: ");
        var snackName = sc.nextLine();
        System.out.print("Snack cost: ");
        var snackCost = Double.parseDouble(sc.nextLine());
        SnackManager.addSnack(new Snack(snackName, snackCost));
        System.out.println("The new snack has been added successfully.");
        SnackManager.showSnacks();
    }

}