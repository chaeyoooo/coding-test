import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int floor = sc.nextInt(); // 계단의 갯수

        int[] dp = new int[floor + 1];
        int[] stair = new int[floor + 1];
        for(int i = 1; i <= floor; i++){
            stair[i] = sc.nextInt();
        }
        //초기 식
        dp[1] = stair[1];
        // floor가 2 이상일때 실행되게
        if(floor >= 2){
            dp[2] = stair[1] + stair[2];
        }
        // floor가 3 이상일때 실행되게
        if(floor >= 3){
            dp[3] = Math.max(stair[1] + stair[3] , stair[2] + stair[3]);
        }

        // dp 테이블 채우기
        for(int i = 4; i <= floor; i++){
            dp[i] = Math.max(dp[i-2] + stair[i] , dp[i-3] + stair[i-1] + stair[i]);
        }

        System.out.println(dp[floor]);
    }
}
