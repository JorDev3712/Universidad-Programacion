import java.util.Scanner;

class MainSeasons {
    public static void main(String[] args) {
        System.out.println("*** Identifies the Season Year ***");
        var scannerConsole = new Scanner(System.in);
        System.out.print("Provides the calendar month: ");
        var month = Integer.parseInt(scannerConsole.nextLine());
        scannerConsole.close();
        if (month == 1 | month == 2 | month == 12){
            System.out.println("We are in The Winter Season!");
        } else if (month == 3 | month == 4 | month == 5){
            System.out.println("We are in The Spring Season!");
        } else if (month == 6 | month == 7 | month == 8){
            System.out.println("We are in The Summer Season!");
        } else if (month == 9 | month == 10 | month == 11){
            System.out.println("We are in The Autumn Season!");
        }else{
            System.out.println("Season unknown");
        }
    }
}
