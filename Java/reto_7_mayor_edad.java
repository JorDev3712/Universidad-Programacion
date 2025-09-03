import java.util.Scanner;

class MainAdultAge {
    public static void main(String[] args) {
        final var AdultAge = 18;
        var scannerConsole = new Scanner(System.in);
        System.out.println("*** Adult Age Identifier ***");
        System.out.print("Provies your age: ");
        var age = Integer.parseInt(scannerConsole.nextLine());
        scannerConsole.close();
        if (AdultAge > age){
            System.out.println(String.format("The person with %d years is minor age", age));
        }else{
            System.out.println(String.format("The person with %d years is major age", age));
        }
    }
}
