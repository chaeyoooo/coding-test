// 백트래킹 부족 에바임 .. 하

import java.util.Scanner;

public class Main {
    static int[][] map;
    static boolean[][] visited;
    static int N;
    static int answer = Integer.MAX_VALUE;
    // 8방 탐색 적용
    static int[] dr = {0,-1,0,1};
    static int[] dc = {1 , 0 , -1 , 0};

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();

        // 초기값 세팅
        map = new int[N][N];
        visited = new boolean[N][N];
        // 화단을 입력받아요
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                map[i][j] = sc.nextInt();
            }
        }
        dfs(0,0);
        System.out.println(answer);
    }

    private static void dfs(int count, int cost) {
        if(count == 3){
            answer = Math.min(answer , cost);
            return;
        }

        // 맨 윗칸 , 아랫 칸 다 제거
        for(int i = 1; i < N -1; i++){
            for(int j = 1; j < N-1; j++){
                if ((checked(i,j))){ // 심을 수 있다면
                    int price = getCost(i,j);
                    setFlower(i,j,true); // 꽃 심기
                    dfs(count + 1 , cost + price);
                    setFlower(i,j,false); // 복구
                }
            }
        }
    }
    static boolean checked(int r , int c){
        // 중심 방문 false
        if(visited[r][c]) return false;

        for(int d = 0; d < 4; d++){
            int nr = r + dr[d];
            int nc = c + dc[d];

            if(visited[nr][nc]) return false;

            if (nr < 0 || nc < 0 || nr >= N || nc >= N) return false;

        }
        return true;
    }

    // 꽃을 심자 !
    static void setFlower(int r, int c , boolean state){
        // state가 true이면 심기 , false면 되돌려라 !
        visited[r][c] = state;
        for(int d = 0; d < 4; d++){
            int nr = r + dr[d];
            int nc = c + dc[d];
            visited[nr][nc] = state;
        }
    }
    static int getCost(int r, int c){
        int sum = map[r][c];
        for (int d = 0; d < 4; d++) {
            int nr = r + dr[d];
            int nc = c + dc[d];
            sum += map[nr][nc];
        }
        return sum;
    }
}
