import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    static int N; // 노드의 갯수
    static int[] parent;
    static int[] depth;
    static boolean[] checked;
    static ArrayList<Integer>[] graph;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt(); // 테스트 케이스 갯수

        for(int tc = 0; tc < T; tc++){
            int N = sc.nextInt(); // 노드의 갯수

            // 선언
            parent = new int[N + 1];
            depth = new int[N + 1];
            graph = new ArrayList[N + 1];
            checked = new boolean[N + 1];

            // 각각 리스트 초기화
            for (int i = 1; i <= N; i++) {
                graph[i] = new ArrayList<>();
            }

            for(int i = 0; i < N -1; i++){
                int p = sc.nextInt(); // 부모
                int c = sc.nextInt(); // 자식

                parent[c] = p; // 자식의 부모 저장
                graph[p].add(c);
                checked[c] = true; // 부모 있음 체크
            }

            int root = 1;
            for(int i = 1; i <= N; i++){
                if(!checked[i]){
                    root = i;
                    break;
                }
            }
            // 깊이 설정
            dfs(root,0);

            int a = sc.nextInt();
            int b = sc.nextInt();

            System.out.println(lca(a,b));
        }
    }
    // lca 알고리즘 공부 후 풀이
    private static int lca(int a, int b) {
        while (depth[a] > depth[b]){
            a = parent[a];
        }

        while(depth[b] > depth[a]){
            b = parent[b];
        }

        while (a != b){
            a = parent[a];
            b = parent[b];
        }
        return a;
    }

    private static void dfs(int root, int i) {
        depth[root] = i;
        for(int child : graph[root]){
            dfs(child, i+1);
        }
    }
}
