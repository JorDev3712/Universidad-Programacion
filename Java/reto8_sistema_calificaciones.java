import java.util.Scanner;

class MainRatingSystem {
    public static void main(String[] args) {
        System.out.println("*** Rating System (PERU) ***");
        var scannerConsole = new Scanner(System.in);
        System.out.print("Provides your rate: ");
        var rate = Integer.parseInt(scannerConsole.nextLine());
        scannerConsole.close();
        
        if (rate >= 17 && rate <= 20){
            System.out.println("You get AD");
        } else if (rate >= 14 && rate <= 16){
            System.out.println("You get A");
        } else if (rate >= 11 && rate <= 13){
            System.out.println("You get B");
        } else if (rate >= 0 && rate <= 10){
            System.out.println("You get C");
        } else{
            System.out.println("Unknown Value");
        }
    }
}