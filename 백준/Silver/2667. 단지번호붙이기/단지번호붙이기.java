
import java.util.*;

public class Main {
    static int N; // 행 열의 갯수
    static int[][] map; // 지도
    static boolean[][] visited; // 방문 지도

    // 방향 벡터
    static int[] dr = { -1 , 1 , 0 , 0};
    static int[] dc = { 0 , 0 , -1 , 1};

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt(); // 행 열의 갯수 받기
        sc.nextLine(); // 주의 주의 주의 주의 
        // 맵 초기화
        map = new int[N][N];

        // 방문 배열 초기화
        visited = new boolean[N][N];

        for(int i = 0; i < N ; i++){
            String line = sc.nextLine();
            for(int j = 0; j < N ; j++){
                map[i][j] = line.charAt(j) - '0';
            }
        }

        int answer = 0;
        List<Integer> list = new ArrayList<>();
        for(int i = 0; i < N ; i++){
            for(int j = 0; j < N  ; j++){
                if(map[i][j] == 1 && !visited[i][j]){
                    list.add(bfs(i,j));
                    answer++;
                }
            }
        }
        System.out.println(answer);
        Collections.sort(list);
        for(int i = 0; i < list.size(); i++){
            System.out.println(list.get(i));
        }
    }

    public static int bfs(int sr, int sc){
        Queue<int[]> queue = new LinkedList<>();
        // 큐에 삽입
        queue.add(new int[]{sr, sc});
        // 방문처리
        visited[sr][sc] = true;

        // 1의 갯수
        int count = 1;

        while(!queue.isEmpty()){
            // 이웃 순회
            int[] curr = queue.poll(); // 현재값 뽑기
            int r = curr[0];
            int c = curr[1];

            for(int i = 0; i < 4; i++){
                int nr = r + dr[i];
                int nc = c + dc[i];

                // 안되는 것 처리
                if(nr < 0 || nc < 0 || nr >= N || nc >= N) continue;
                if(map[nr][nc] == 0) continue;
                if(visited[nr][nc]) continue;

                queue.add(new int[]{ nr, nc});
                visited[nr][nc] = true;
                count++;
            }
        }
        return count;
    }
}
