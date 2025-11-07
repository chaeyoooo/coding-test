

import java.util.Scanner;

public class  Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int M = sc.nextInt();

        int[][] arr = new int[N ][M ];

        for(int i = 0; i < N ; i++){
            for(int j = 0; j < M; j++){
                arr[i][j] = sc.nextInt();
            }
        }

//        for(int i = 1; i < N  + 1; i++){
//            for(int j = 0; j < M + 1; j++){
//                System.out.println(arr[i][j]);
//            }
//        }

        int K = sc.nextInt();

        for(int o = 0; o < K; o++){
            int i = sc.nextInt() - 1; // 1
            int j = sc.nextInt() - 1; // 1
            int x = sc.nextInt() - 1; // 2
            int y = sc.nextInt() - 1; // 3

            int sum = 0;
            for(int a = i; a <= x; a++){ // 1 ~ 2
                for(int b = j; b <= y; b++){ // 1 ~ 3
                    sum += arr[a][b];
                }
            }
            System.out.println(sum);
        }
    }
}
