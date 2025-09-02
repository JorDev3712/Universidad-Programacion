import java.util.Scanner;

class MainPresentation {
    public static void main(String[] args) {
        System.out.println("*** Introduce yourself to more detail ***");
        Scanner scannerConsole = new Scanner(System.in);
        System.out.print("Write your name: ");
        String name = scannerConsole.nextLine();
        System.out.print("Write your age: ");
        Integer edad = Integer.parseInt(scannerConsole.nextLine());
        System.out.print("Are you an only child? (y-n): ");
        String line = scannerConsole.nextLine();
        Boolean onlyChild = line == "y";
        System.out.print("What is your favorite drink?: ");
        String drink = scannerConsole.nextLine();
        System.out.print("How much does your favorite drink cost?: ");
        Float cost = Float.parseFloat(scannerConsole.nextLine());
        scannerConsole.close();

        System.out.printf("Hola %s, tienes %d años, tu bebida favorita es %s con costo: %f \n", name, edad, drink, cost);
        System.out.printf("Además, eres hijo unico: %b", onlyChild);
    }
}