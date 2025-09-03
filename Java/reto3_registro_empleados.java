import java.util.Scanner;

class MainEmployee{
    public static void main(String[] args) {
        System.out.println("*** Employee  Registration ***");
        Scanner scannerConsole = new Scanner(System.in);
        System.out.print("Provides your name: ");
        String name = scannerConsole.nextLine();
        System.out.print("Provides your age: ");
        Integer age = Integer.parseInt(scannerConsole.nextLine());
        System.out.print("Provides your salary (USD): ");
        Integer salary = Integer.parseInt(scannerConsole.nextLine());
        System.out.print("Are you a trusted employee? (true/false): ");
        Boolean trusted = Boolean.parseBoolean(scannerConsole.nextLine());
        scannerConsole.close();
        System.out.println("The information provided is: ");
        System.out.println(String.format("Name: %s", name));
        System.out.println(String.format("Age: %d", age));
        System.out.println(String.format("Salary: %d (USD)", salary));
        System.out.println(String.format("Trusted Employee: %b", trusted));
    }
}