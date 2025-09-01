import java.util.Scanner;

class DetalleLibro {
    public static void main(String[] args) {
        // Enter values via console
        Scanner scannerConsole = new Scanner(System.in);
        System.out.println("*** Book Detail ***");
        System.out.print("Provides the title: ");
        String bookTitle = scannerConsole.nextLine();
        System.out.print("Provides the author: ");
        String bookAuthor = scannerConsole.nextLine();
        scannerConsole.close();

        // Then we send it to print to the console
        System.out.printf("%s was written by %s", bookTitle, bookAuthor);
    }
}