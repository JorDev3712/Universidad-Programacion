import java.util.Scanner;

class MainMaxNumber {
    public static void main(String[] args) {
        // We print the title on the console
        System.out.println("*** Identifies the largest of two numbers ***");
        var scannerConsole = new Scanner(System.in);
        System.out.print("Provides the first number: ");
        var firstNumber = Integer.parseInt(scannerConsole.nextLine());
        System.out.print("Provides the second number: ");
        var secondNumber = Integer.parseInt(scannerConsole.nextLine());
        scannerConsole.close();
        if (firstNumber > secondNumber){
            System.out.println("The largest number is: " + firstNumber);
        }else if (secondNumber > firstNumber){
            System.out.println("The largest number is: " + secondNumber);
        }else {
            System.out.println("The numbers are equal.");
        }
    }
}