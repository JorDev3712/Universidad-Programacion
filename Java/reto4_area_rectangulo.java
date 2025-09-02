// En realidad se escribe CalculateMainRentagle

import java.util.Scanner;

class MainCalculateRentagle {
    public static void main(String[] args) {
        System.out.println("*** Calculating the area of a rectangle ***");
        var scannerConsole = new Scanner(System.in);
        System.out.print("Provides the base: ");
        Float rec_base = Float.parseFloat(scannerConsole.nextLine());
        System.out.print("Provides the height: ");
        Float rec_height = Float.parseFloat(scannerConsole.nextLine());
        Float area = rec_base * rec_height;
        System.out.println(String.format("The Area of a rectangle is: %f", area));
    }
}
