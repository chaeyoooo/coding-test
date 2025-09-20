import java.util.Scanner;
import java.util.Arrays;

public class Main {
    static int N;
    static final int INF = Integer.MAX_VALUE;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt(); // 정점 간선
        int[][] adj = new int[N][N]; // 인접 행렬

        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                adj[i][j] = sc.nextInt();
            }
        }

        int[] p = new int[N]; // 부모
        int[] dist = new int[ N ]; // 가중치 저장 배열
        boolean[] visited = new boolean[N ]; // 트리인지 아닌지 판단

        // 1. 가중치 배열 초기화
        Arrays.fill(dist , INF);
        Arrays.fill(p,-1);

        // 2. 시작 정점을 골라라
        dist[0] = 0;
        long ans = 0;

        // 3. 전체 반복문을 수행하면서 정점을 뽑겠다
        for(int i = 0; i < N; i++){
            int min = INF;
            int idx = -1;
            for(int j = 0; j < N; j++){
                if(!visited[j] && dist[j] < min){
                    min = dist[j];
                    idx = j;
                }
            }

            visited[idx] = true;

            for(int j = 0; j < N ; j++){
                if(!visited[j] && dist[j] > adj[idx][j]){
                    dist[j] = adj[idx][j];
                    p[j] = idx;
                }
            }
        }

        for(int i = 0; i < N ; i++){
            ans += dist[i];
        }
        System.out.println(ans);
    }
}
