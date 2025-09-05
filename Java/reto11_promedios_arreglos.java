import java.util.Scanner;

class MainRatings {
    public static void main(String[] args) {
        System.out.println("**** Average of Rating ***");
        var sc = new Scanner(System.in);
        System.out.print("How many ratings do you want to add?: ");
        var total = Integer.parseInt(sc.nextLine());
        var ratings = new int[total];
        for (var i = 0; i < total; i++){
            System.out.print(String.format("Rate[%d] = ", i));
            var value = Integer.parseInt(sc.nextLine());
            ratings[i] = value;
        }

        var sum = 0;
        for (var i = 0; i < ratings.length; i++){
            sum += ratings[i]; 
        }

        var rate = sum / total;
        System.out.println("Average of the ratings: " + rate);

        sc.close();
    }
}