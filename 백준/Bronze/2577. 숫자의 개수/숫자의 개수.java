
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int A = sc.nextInt(); // 150
        int B = sc.nextInt(); // 266
        int C = sc.nextInt(); // 427

        int result = A * B * C;
        String answer  = Integer.toString(result); // 17037300

        // 정답 배열
        int[] arr = new int[10];
        for(int i = 0; i < answer.length(); i++){ // 8개 길이 돌면서
            for(int j = 0; j < 10; j++){
                if(answer.charAt(i) == Integer.toString(j).charAt(0)){ // 이부분 int에서 char
                    arr[j]++;
                }
            }
        }
        for(int k = 0;  k < arr.length; k++){
            System.out.println(arr[k]);
        }
    }
}
