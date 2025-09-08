import java.util.Random;
import java.util.Scanner;

class MainUniqueIdGenerator {
    public static void main(String[] args) {
        System.out.println("*** Unique Id Generator ***");
        var sc = new Scanner(System.in);
        System.out.print("What is your name?: ");
        var name = sc.nextLine();
        System.out.print("What is your lastname?: ");
        var lastname = sc.nextLine();
        System.out.print("What is your date of birth? (YYYY): ");
        var year = sc.nextLine();
        sc.close();

        var unique = name.substring(0, 2) + lastname.substring(0, 2) + year.substring(year.length() - 2);
        var random = new Random();
        unique += random.nextInt(0, 9999);
        unique = unique.toUpperCase();
        System.out.println("Congratulations! Your new unique id number is: " + unique);
    }
}