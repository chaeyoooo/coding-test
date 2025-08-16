

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt(); // 5
        int M = sc.nextInt(); // 3



        // A 배열 만들어주기
        int[] A = new int[N + 1];
        A[0] = 0;
        for(int i = 1; i < N + 1; i++){
            A[i] = sc.nextInt();
        }

        // 구간합 배열 만들기
        int[] S = new int[N + 1];
        S[0] = 0;
        for(int j = 1; j < N+1; j++){
            S[j] = S[j-1] + A[j];
        }

        // 질의 갯수 저장
        for(int i = 0; i < M; i++){
            int a = sc.nextInt();
            int b = sc.nextInt();

            int result = S[b] -S[a-1];
            System.out.println(result);
        }
    }
}
