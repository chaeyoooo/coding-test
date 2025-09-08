

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
    // i didn't know that how to solve bfs
    // so , fist gpt help me but coding is myself

    static int N,M;
    static int[][] map;
    static boolean [][] visited;

    // 방향 벡터
    static int[] dr = { -1 , 1 , 0 , 0};
    static int[] dc = { 0 , 0 , -1 , 1};

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        M = sc.nextInt();

        // 맵 선언
        map = new int[N][M];

        // 방문 선언
        visited = new boolean[N][M];

        // 맵 숫자 받기
        for(int i = 0; i < N; i++){
            for(int j = 0; j < M; j++){
                map[i][j] = sc.nextInt();
            }
        }
        int picture = 0;
        int max_one_count = 0;

        // 그림의 갯수 -> 1의 부분의 갯수를 구해라
        for(int i = 0; i < N; i++){
            for(int j = 0; j < M; j++){
                if(map[i][j] == 1 && !visited[i][j]){
                    picture++;
                    int one_count = bfs(i,j);
                    max_one_count = Math.max(max_one_count, one_count);
                }
            }
        }
        System.out.println(picture);
        System.out.println(max_one_count);
    }

    static int bfs(int sr , int sn){
        Queue<int[]> queue = new LinkedList<>();
        // 큐에 삽입
        queue.add(new int[]{sr , sn});
        // 방문 처리
        visited[sr][sn] = true;

        // 1의 갯수를 세는 변수
        int one_cnt = 1;

        while(!queue.isEmpty()){
            // 큐가 비어있지 않을때
            int[] cur = queue.poll(); // 큐에 현재값 빼기
            int r = cur[0]; // 현재 sr값
            int c = cur[1]; // 현재 sc값

            // 인접 배열 확인하기
            for(int d = 0; d < 4; d++){
                int nr = r+ dr[d];
                int nc = c + dc[d];

                if(nr < 0 || nc < 0 || nr >= N || nc >= M) continue;
                if(map[nr][nc] == 0) continue;
                if(visited[nr][nc]) continue;

                // 큐에 인접 배열 넣어주기
                queue.add(new int[] {nr,nc});
                visited[nr][nc] = true;
                one_cnt++;
            }

        }
        return one_cnt;
    }
}
