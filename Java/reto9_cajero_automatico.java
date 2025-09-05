import java.util.Scanner;

class MainATM {
    public static void main(String[] args) {
        System.out.println("*** Automated Treller Machine ***");
        Double balance = 2000.0;
        var scannerConsole = new Scanner(System.in);
        var exit = false;
        while (!exit) {
            System.out.print("""
                    Menu:
                    1. Check Balance.
                    2. Withdraw balance.
                    3. Deposit balance.
                    4. Exit.
                    Choose an option:\s""");
            var option = Integer.parseInt(scannerConsole.nextLine());
            switch (option) {
                case 1 -> System.out.println("Your current balance is: $" + balance);
                case 2 -> {
                    System.out.print("Enter the amount to withdraw: ");
                    var amount = Double.parseDouble(scannerConsole.nextLine());
                    if (amount <= 0){
                        System.out.println("You can't withdraw a negative or zero amount.");
                    }
                    else if (amount > balance){
                        System.out.println("You don't have enough balance.");
                    } else{
                        balance -= amount;
                        System.out.println("Your new balance is: $" + balance);
                    }
                }
                case 3 -> {
                    System.out.print("Enter the amount to deposit: ");
                    var deposit = Double.parseDouble(scannerConsole.nextLine());
                    if (deposit <= 0){
                        System.out.println("You can't deposit a negative or zero amount.");
                    }else{
                        balance += deposit;
                        System.out.println("Your new balance is: $" + balance);
                    }
                }
                case 4 -> {
                    System.out.println("Closing the system...See you soon!");
                    exit = true;
                }
            
                default -> System.out.println("Invalid option.");
            }
        }
        scannerConsole.close();
    }
}
