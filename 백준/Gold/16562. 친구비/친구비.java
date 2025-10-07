import java.util.LinkedList;
import java.util.Scanner;

public class Main {
    static int[][] parent;
    static int k;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt(); // 학생 수
        int M = sc.nextInt(); // 친구 관계 수
        k = sc.nextInt();

        parent = new int[2][N + 1];

        for (int i = 1; i < N + 1; i++) {
            parent[0][i] = i; // 인덱스 값을 넣고
            parent[1][i] = sc.nextInt(); // 돈을 넣으세요!
        }

        // 친구 관계
        for (int i = 0; i < M; i++) {
            int v = sc.nextInt();
            int w = sc.nextInt();

            union(v, w);
        }
        // 합집합 한 것을 parent가 받게 설정
        for (int i = 1; i < N; i++) {
            parent[0][i] = find(i);
        }
        // 정렬로 해보다가 안돼서 gpt한테 이 부분 도움 .. ( 도움을 최대한 안받아보자 !)
        int answer = 0;
        for (int i = 1; i <= N; i++) {
            int root = parent[0][i]; // 인덱스를 잡고 -> 1

            if (root == i) {
                int mincost = parent[1][i]; // 10 , 20
                // 최솟값 찾아내는 것
                for (int j = 1; j <= N; j++) {
                    if (parent[0][j] == i) {
                        mincost = Math.min(mincost, parent[1][j]);
                    }
                }
                answer += mincost;
            }
        }
        if (answer <= k) {
            System.out.println(answer);
        }else{
            System.out.println("Oh no");
        }
    }

        // 부모 찾는 메서드
        private static int find ( int x){
            if (parent[0][x] == x) {
                return x;
            }
            return parent[0][x] = find(parent[0][x]);
        }

        // 합치는 메서드
        private static void union ( int a, int b){
            a = find(a);
            b = find(b);

            if (a != b) {
                if (a < b) {
                    parent[0][b] = a;
                } else {
                    parent[0][a] = b;
                }
            }
        }
    }
