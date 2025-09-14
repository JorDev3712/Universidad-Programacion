package proyecto_maquina_snacks.v2.presentation;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

import proyecto_maquina_snacks.v2.dominion.Snack;
import proyecto_maquina_snacks.v2.services.IServicioSnacks;
import proyecto_maquina_snacks.v2.services.ServicioSnacks;

class MainSnackMachine {
    public static void main(String[] args) {
        snackMachine();
    }

    public static void snackMachine(){
        System.out.println("*** Snack Machine ***");

        // We save client productos
        List<Snack> products = new ArrayList<>();
        IServicioSnacks snackService = new ServicioSnacks();
        snackService.initialize();
        snackService.showSnacks();
        System.out.println();

        var sc = new Scanner(System.in);
        var exit = false;
        while (!exit) {
            showMenu();
            var option = Integer.parseInt(sc.nextLine());
            exit = executeOptions(option, sc, snackService, products);
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

    private static Boolean executeOptions(int menuOption, Scanner sc, IServicioSnacks service, List<Snack> clientProductos){
        var exit = false;
        switch (menuOption) {
            case 1 -> buySnack(sc, service, clientProductos);
            case 2 -> showTicket(clientProductos);
            case 3 -> addSnack(sc, service);
            case 4 -> {
                System.out.println("Closing machine... See you soon!");
                exit = true;
            }
            default -> System.out.println("Invalid option...");
        }
        return exit;
    }

    private static void buySnack(Scanner sc, IServicioSnacks service, List<Snack> clientProductos){
        System.out.print("What snack do you want to buy? (id): ");
        var snackId = Integer.parseInt(sc.nextLine());
        var snack = service.getSnack(snackId);
        if (snack != null){
            clientProductos.add(snack);
            System.out.println("Ok, Snack added: " + snack.toString());
        }else {
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

    private static void addSnack(Scanner sc, IServicioSnacks service){
        System.out.println("*** Create a Snack ***");
        System.out.print("Snack name: ");
        var snackName = sc.nextLine();
        System.out.print("Snack cost: ");
        var snackCost = Double.parseDouble(sc.nextLine());
        service.addSnack(snackName, snackCost);
        System.out.println("The new snack has been added successfully.");
        service.showSnacks();
    }

}