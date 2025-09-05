import java.util.Scanner;

class MainDiagonal {
    public static void main(String[] args) {
        System.out.println("*** Matrices ***");
        var sc = new Scanner(System.in);
        System.out.print("Provides the rows: ");
        var rows = Integer.parseInt(sc.nextLine());
        System.out.print("Provides the columns: ");
        var columns = Integer.parseInt(sc.nextLine());
        int[][] matrix = new int[rows][columns];
        // We are requesting the values
        for (var r = 0; r < rows; r++){
            for (var c = 0; c < columns; c++){
                System.out.print(String.format("Enter a value[%d][%d] = ", r, c));
                matrix[r][c] = Integer.parseInt(sc.nextLine());
            }
        }

        // We are looking for the diagonal
        var diagonalSum = 0;
        for (var r = 0; r < rows; r++){
            for (var c = 0; c < columns; c++){
                if (r == c){
                    diagonalSum += matrix[r][c]; 
                }
            }
        }
        System.out.println("Sum diagonal: " + diagonalSum);
    }
}
