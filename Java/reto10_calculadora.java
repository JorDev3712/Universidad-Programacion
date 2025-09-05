import java.util.Scanner;

class MainCalculator {
    public static void main(String[] args) {
        System.out.println("*** Calculator in Java ***");
        var scannerConsole = new Scanner(System.in);
        var exit = false;
        while (!exit) {
            System.out.print("""
                    Menu:
                    1. Plus
                    2. Subtract
                    3. Multiply
                    4. Split
                    5. Exit
                    Choose an option:\s""");
            var option = Integer.parseInt(scannerConsole.nextLine());
            switch (option) {
                case 1 -> {
                    System.out.print("Provides the first number: ");
                    var a = Float.parseFloat(scannerConsole.nextLine());
                    System.out.print("Provides the second number: ");
                    var b = Float.parseFloat(scannerConsole.nextLine());
                    Float plus = a + b;
                    System.out.println("Sum result: " + plus);
                }

                case 2 -> {
                    System.out.print("Provides the first number: ");
                    var a = Float.parseFloat(scannerConsole.nextLine());
                    System.out.print("Provides the second number: ");
                    var b = Float.parseFloat(scannerConsole.nextLine());
                    Float subtract = a - b;
                    System.out.println("Subtract result: " + subtract);
                }

                case 3 -> {
                    System.out.print("Provides the first number: ");
                    var a = Float.parseFloat(scannerConsole.nextLine());
                    System.out.print("Provides the second number: ");
                    var b = Float.parseFloat(scannerConsole.nextLine());
                    Float multiply = a * b;
                    System.out.println("Multiply result: " + multiply);
                }

                case 4 -> {
                    System.out.print("Provides the first number: ");
                    var a = Float.parseFloat(scannerConsole.nextLine());
                    if (a <= 0){
                        System.out.println("The number can't be negative or zero.");
                        break;
                    }

                    System.out.print("Provides the second number: ");
                    var b = Float.parseFloat(scannerConsole.nextLine());
                    if (b <= 0){
                        System.out.println("The number can't be negative or zero.");
                        break;
                    }
                    
                    Float split = a / b;
                    System.out.println("Split result: " + split);
                }

                case 5 -> {
                    System.out.println("Closing the calculator...See you soon!");
                    exit = true;
                }
            
                default -> System.out.println("Invalid option.");
            }
        }
        scannerConsole.close();
    }
}