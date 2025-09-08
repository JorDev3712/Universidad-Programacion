import java.util.Scanner;

class MainMailGenerator {
    public static void main(String[] args) {
        System.out.println("*** Mail Generator ***");
        var sc = new Scanner(System.in);
        System.out.print("What is your name?: ");
        var name = sc.nextLine();
        System.out.print("What is your lastname?: ");
        var lastname = sc.nextLine();
        sc.close();
        var email = (name + "." + lastname + "@example.com").toLowerCase();
        System.out.println("Congratulations! Your email is: " + email);
    }
}
