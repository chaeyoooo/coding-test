
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int M = sc.nextInt();

        char[][] map = new char[N][M];

        // map 채우기
        for(int i = 0; i < N; i++){
            String s  = sc.next();
            for(int j = 0; j < M; j++){
                map[i][j] = s.charAt(j);
            }
        }

        char[][] w = new char[N][M];
        char[][] b = new char[N][M];


        // 첫 시작이 W인 경우
        for(int i = 0; i < N; i++){
               for(int j = 0; j < M; j++){
                   if(i % 2 == 0 && j % 2 == 0){
                       w[i][j] = 'W';
                   }else if( i % 2 != 0 && j % 2 != 0){
                       w[i][j] = 'W';
                   }else{
                       w[i][j] = 'B';
                   }
               }
           }

        for(int i = 0; i < N; i++){
            for(int j = 0; j < M; j++){
                if(i % 2 == 0 && j % 2 == 0){
                    b[i][j] = 'B';
                }else if( i % 2 != 0 && j % 2 != 0){
                    b[i][j] = 'B';
                }else{
                    b[i][j] = 'W';
                }
            }
        }

        int answer = Integer.MAX_VALUE;
        
        // 여기서 비교 
        for(int x = 0; x <= N - 8; x++){
            for(int y = 0; y <= M - 8; y++){

                int w_a = 0;
                int b_a = 0;
                
                for(int i = x; i < x + 8; i++){
                    for(int j = y; j < y + 8; j++){
                        if(map[i][j] != w[i][j]) w_a++;
                        if(map[i][j] != b[i][j]) b_a++;
                    }
                }

                int min = Math.min(w_a, b_a);
                if(min < answer) answer = min;
            }
        }

        System.out.println(answer);
    }
}
