
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
    static int N , M , V;
    static int[][] map;
    static boolean[] visited;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt(); // 정점의 개수
        M = sc.nextInt(); // 간선의 개수
        V = sc.nextInt(); // 탐색 시작 번호

        // 초기화 하기
        map = new int[N + 1][N +1];
        visited = new boolean[N + 1];

        // 입력받기
        for(int i = 0; i < M; i++){
            int start = sc.nextInt();
            int end = sc.nextInt();

            map[start][end] = 1;
            map[end][start] = 1;
        }
        dfs(V);
        System.out.println();

        visited = new boolean[N + 1]; // 방문 배열 초기화 꼭 해주기
        bfs(V);
    }

    static void bfs(int vv){
        Queue<Integer> q = new LinkedList<>();
        q.add(vv); // 시작 정점 넣기
        visited[vv] = true;

        while(!q.isEmpty()){
            int curr = q.poll(); // 현재값 꺼내기 -> 1
            System.out.print(curr + " ");

            // 정점을 돌면서
            for(int i = 1; i <= N; i++){ // 이거 N인것 !!! 실 수 ㄴㄴ
                if(!visited[i] && map[curr][i] == 1){
                    q.add(i);
                    visited[i] = true;
                }
            }
        }
    }

    // Dfs -> gpt의 도움
    static void dfs(int vv){
        visited[vv] = true;
        System.out.print(vv + " ");

        for(int i = 1; i <= N; i++){
            if(!visited[i] && map[vv][i] == 1){
                dfs(i);
            }
        }
    }
}
