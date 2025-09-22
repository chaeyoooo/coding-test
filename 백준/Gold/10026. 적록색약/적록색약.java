import java.util.Scanner;

public class Main {

    static int N; // 열과 행
    static char[][] map;
    static char[][] eyesmap;
    static boolean[][] visited;
    static boolean[][] eyesvisited;

    static int[] dr = { -1 , 1  , 0 , 0}; // 방향 탐색
    static int[] dc = { 0 , 0 , -1 , 1}; // 방향 탐색

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt(); // 열과 행 받기

        // 초기 배열 선언해주기
        map = new char[N][N];
        eyesmap = new char[N][N];
        visited = new boolean[N][N];
        eyesvisited = new boolean[N][N];

        for(int i = 0; i < N; i++){
            String s =  sc.next();
            for(int j = 0; j < N; j++){
                // i와 j 열과 행 선언
                map[i][j] = s.charAt(j);
                eyesmap[i][j] = s.charAt(j);

                if(eyesmap[i][j] == 'G'){
                    eyesmap[i][j] = 'R';
                }
            }
        }

        int answer = 0;
        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                if(map[i][j] == 'R' && !visited[i][j]){
                    bfs(i,j);
                    answer++;
                } else if (map[i][j] == 'G' && !visited[i][j]) {
                    bfs(i,j);
                    answer++;
                }else if(map[i][j] == 'B' && !visited[i][j]){
                    bfs(i,j);
                    answer++;
                }
            }
        }

        int result = 0;
        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                if(eyesmap[i][j] == 'R' && !eyesvisited[i][j]){
                    eyesbfs(i,j);
                    result++;
                } else if (map[i][j] == 'B' && !eyesvisited[i][j]) {
                    eyesbfs(i,j);
                    result++;
                }
            }
        }
        System.out.println(answer);
        System.out.println(result);
    }

    public static void bfs(int r , int c){
        visited[r][c] = true;

        // 4방 탐색 진행
        for(int d = 0; d < 4; d++){
            int nr = r + dr[d];
            int nc = c + dc[d];

            if(nr >= 0 && nc >= 0 && nr < N && nc < N){
                if(map[r][c] == 'R' && map[nr][nc] == 'R' && !visited[nr][nc]){
                    bfs(nr, nc);
                } else if (map[r][c] == 'B' && map[nr][nc] == 'B' && !visited[nr][nc]){
                    bfs(nr, nc);
                } else if(map[r][c] == 'G' && map[nr][nc] == 'G' && !visited[nr][nc]){
                    bfs(nr,nc);
                }
            };
        }
    }

    public static void eyesbfs(int r , int c){
        eyesvisited[r][c] = true;

        // 4방 탐색 진행
        for(int d = 0; d < 4; d++){
            int nr = r + dr[d];
            int nc = c + dc[d];

            if(nr >= 0 && nc >= 0 && nr < N && nc < N){
                if(eyesmap[r][c] == 'R' && eyesmap[nr][nc] == 'R' && !eyesvisited[nr][nc]){
                    eyesbfs(nr, nc);
                } else if (eyesmap[r][c] == 'B' && eyesmap[nr][nc] == 'B' && !eyesvisited[nr][nc]){
                    eyesbfs(nr, nc);
                }
            };
        }
    }
}
