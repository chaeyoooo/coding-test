import java.util.Scanner;

// 백트래킹 -> 부족
public class Main {
    static int N, M;
    static int[] arr;
    static boolean[] visited;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        M = sc.nextInt();

        arr = new int[M];
        visited = new boolean[N + 1];
        dfs(0);
        System.out.println(sb.toString());
    }

    static void dfs(int depth) {
        if (depth == M) {
            for (int i = 0; i < M; i++) {
                sb.append(arr[i]).append(' ');
            }
                sb.append('\n');
                return;
            }

            for (int i = 1; i <= N; i++) {
                if(!visited[i]){
                    arr[depth] = i;
                    visited[i] = true;
                    dfs(depth + 1);
                    visited[i] = false;
                }
            }
        }
    }

