
import java.util.Scanner;

public class Main {
    static int N;
    static int[] arr;
    static boolean[] visited;
    static int[] answer;
    static int max;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        arr = new int[N];
        answer = new int[N];
        visited = new boolean[N];
        for(int i = 0; i < N; i++){
            arr[i] = sc.nextInt();
        }
        perm(0);
        System.out.println(max);

    }
    static void perm(int depth){
        if(depth == N){
            int result = 0;
            for(int i = 2; i <= N ; i++){
                result += Math.abs(answer[i-2] - answer[i -1]);
            }
            max = Math.max(max , result);
            return;
        }

        for(int i = 0; i < N; i++){
            if(!visited[i]){
                visited[i] = true;
                answer[depth] = arr[i];
                perm(depth +1);
                visited[i] = false;
            }
        }
    }
}
