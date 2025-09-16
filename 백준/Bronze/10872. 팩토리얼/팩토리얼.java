
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        System.out.println(recursive(N));
    }

    private static int recursive(int n) {
        if( n <= 1){
            return 1;
        }
        for(int i = n; i > 1; i--){
            return n * recursive(n-1);
        }
        return n;
    }
}
