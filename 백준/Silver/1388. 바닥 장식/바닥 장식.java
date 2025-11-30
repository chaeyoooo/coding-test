import java.util.Scanner;

public class Main{
    public static void main(String[] args) {
        // 형택 건축가
        // 기훈이의 집 완성
        // 기훈이의 방 : 직사각형 모형 , 방 안에는 벽과 평행한 모양의 정사각형
        // 바닥장식 디자인
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int M = sc.nextInt();

        // 가로 판자의 경우 : 바로 왼쪽이 - 라면 새로운 판자 X
        // 새로 판자의 경우 : 바로 위가 | 라면 새로운 판자 X

        // board 채우기
        char[][] board = new char[N][M];

        for(int i = 0; i < N; i++){
            String s = sc.next();
            for(int j = 0; j < M; j++){
                board[i][j] = s.charAt(j);
            }
        }

        // board 채운 후에 가로 , 세로 판자 확인하기
        int count1 = 0;
        int count2 = 0;
        for(int i = 0; i < N; i++){
            for(int j = 0; j < M ; j++){
                if(board[i][j] == '-'){
                    if(j == 0 || board[i][j - 1] != '-'){
                        count1++;
                    }
                }
            }
        }

        for(int i = 0; i < N; i++){
            for(int j = 0; j < M ; j++){
                if(board[i][j] == '|'){
                    if(i == 0 || board[i - 1][j] != '|'){
                        count2++;
                    }
                }
            }
        }

        System.out.println(count1 + count2);
    }
}