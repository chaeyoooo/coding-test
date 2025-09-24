import java.util.LinkedList;
import java.util.Scanner;

public class Main {
    static int[][] map;
    static boolean[] visited;
    static int[] parent;
    static int N , del , count;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        LinkedList<int[]> list = new LinkedList<>();

        N = sc.nextInt();

        map = new int[N + 1][N + 1];
        visited = new boolean[N + 1];
        for(int i = 0; i < N; i++){
            list.add(new int[]{sc.nextInt() , i}); // 배열에 받는 값과 인덱스 값을 넣어줌
        }

        del = sc.nextInt(); // 삭제

        // map에 넣기
        int root = -1;
        for(int i = 0; i < N; i++){
            if(list.get(i)[0] == -1) {
                root = list.get(i)[1]; // 루트 저장
                continue;
            }
            map[list.get(i)[0]][list.get(i)[1]] = 1; // -1이면 넘기고 그게 아니라면 map에 넣어줘!
        }
        dfs(root);
        System.out.println(count);
    }
    static void dfs(int node){
        //삭제 부분을 0으로 대체 생각햇지만 자식 노드까지 0이 되지 않기에 문제가 있었음 -> 이 삭제 부분을 어떻게 할지 도움  도움
        if(node == del) return; // 바로 삭제 해서 자식 노드 보지 않게 

        visited[node] = true;

        boolean baby = true;
        for(int i = 0; i < N; i++){
            if(map[node][i] == 1 && !visited[i] && i != del){
                baby = false;
                dfs(i);
            }
        }
        if(baby) count++;
    }
}
