
import java.util.LinkedList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {
    static int N,K;
    static boolean[] visited;
    static int[] result;
    static List<int[]> exercise = new LinkedList<>();
    static int answer = 0;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 입력받기
        N = sc.nextInt(); // 3
        K = sc.nextInt(); // 4

        visited = new boolean[N];
        result = new int[N];

        // 운동기구 번호랑 중랑을 받는다
        for(int i = 0; i < N; i++){
            int w = sc.nextInt();
            exercise.add(new int[]{ i + 1, w - K});
        }

        perm(0,500);
        System.out.println(answer);
    }

    static void perm(int depth, int power){
        if(depth == N){
            answer++;
            return;
        }
        for(int i = 0; i < N; i++){
            if(!visited[i]){
                int nextPower = power + exercise.get(i)[1];

                // 근력 500 이하면 패스
                if(nextPower < 500) {
                    continue;
                }

                visited[i] = true;
                result[depth] = exercise.get(i)[0];
                perm(depth +1 , nextPower);
                visited[i] = false;
            }
        }
    }
}
