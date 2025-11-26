import java.util.*;

public class Main{
    // bfs 기억 안나서 gpt 약 도움 ㅎ..
    static boolean[][] visited;
    static int[][] map;
    static int[] dr = { -1 , 1 , 0 , 0 };
    static int[] dc = { 0 , 0 , -1 , 1 };
    static int M, N, K;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        M = sc.nextInt(); // 행
        N = sc.nextInt(); // 열
        K = sc.nextInt(); // 줄의 수

        // 먼저 배열의 크기
        map = new int[M][N];

        visited = new boolean[M][N];

        // map이 칠해져 있는 것은 1로 만들기
        for(int i = 0; i < K; i++){
            int firstX = sc.nextInt(); // 0
            int firstY = sc.nextInt(); // 2
            int lastX = sc.nextInt(); // 4
            int lastY = sc.nextInt(); // 4

            for(int x = firstX; x < lastX; x++){
                for(int y = firstY; y < lastY; y++){
                    map[y][x] = 1;
                }
            }
        }

        List<Integer> result = new ArrayList<>();

        for(int i = 0; i < M; i++){
            for(int j = 0; j < N; j++){
                if(map[i][j] == 0 && !visited[i][j]){
                    int answer = bfs(i,j);
                    result.add(answer);
                }
            }
        }
        Collections.sort(result);
        System.out.println(result.size());
        for(int i = 0; i < result.size(); i++){
            System.out.print(result.get(i) + " ");
        }
        System.out.println();
    }
    private static int bfs(int r, int c){
        Queue<int[]> queue = new LinkedList<>();
        int answer = 1;
        queue.add(new int[] {r,c });
        visited[r][c] = true;

        while(!queue.isEmpty()){
            int[] cur = queue.poll();

            // 방향 탐색
            for(int i = 0; i < 4; i++){
                int nr = cur[0] + dr[i];
                int nc = cur[1] + dc[i];

                if(nr < 0 || nr >= M || nc < 0 || nc >= N) continue;
                if(visited[nr][nc]) continue;
                if(map[nr][nc] == 1) continue;

                answer++;
                queue.add(new int[] { nr , nc });
                visited[nr][nc] = true;
            }
        }
        return answer;
    }
}
