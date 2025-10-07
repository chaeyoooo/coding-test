import java.util.Scanner;

public class Main {

    static int N, M,count;
    static int[][] map;
    static boolean [][] viisted;
    static boolean ischecked;

    // 방향 벡터
    static int[] dr = {-1, -1, 0, 1, 1, 1, 0, -1};
    static int[] dc = {0, 1, 1, 1, 0, -1, -1, -1};
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        M = sc.nextInt();

        // 초기화
        map  = new int[N][M];
        viisted = new boolean[N][M];

        for(int i = 0; i < N; i++){
            for(int j = 0; j < M; j++){
                map[i][j] = sc.nextInt();
            }
        }

        for(int i = 0; i < N; i++){
            for(int j = 0; j < M; j++){
                if(map[i][j] != 0 && !viisted[i][j]){
                    ischecked = true;
                    dfs(i,j,map[i][j]);
                    if(ischecked){
                        count++;
                    }
                }
            }
        }
        System.out.println(count);
    }

    private static void dfs(int r, int c , int height) {
        viisted[r][c] = true;

        for(int d = 0; d < 8; d++){
            // 새롭게 갱신
            int nr = r + dr[d];
            int nc = c + dc[d];

            if(nr >= 0 && nc >= 0 && nr < N && nc < M){
                if(map[nr][nc] > height){
                    ischecked = false;
                }

                if(map[nr][nc] == height && !viisted[nr][nc]){
                    dfs(nr,nc , height);
                }
            }
        }
    }
}
