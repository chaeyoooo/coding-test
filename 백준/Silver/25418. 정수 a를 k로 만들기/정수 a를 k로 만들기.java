import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
    // 다시 풀어봐야할듯 가지치기 문제 ( 아직도 문제가 ... )
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int A = sc.nextInt();
        int K = sc.nextInt();

        // 5 17

        boolean[] visited = new boolean[K + 1];
        Queue<int[]> q = new LinkedList<>();

        q.add(new int[]{A,0}); // queue = [( 5, 0 )]
        visited[A] = true; // visited[5] = true

        while(!q.isEmpty()){
            int[] cur = q.poll();
            int x = cur[0]; // 현재 숫자 -> 5
            int cnt = cur[1]; // 지금까지 연산 횟수 -> 0

            if(x == K){
                System.out.println(cnt);
                return;
            }

            if(x + 1 <= K && !visited[x+1]){ // 6 <= 17 && !visited[6]
                visited[x + 1] = true; // visited[6] = true
                q.add(new int[] { x + 1 , cnt + 1}); // ( 6 , 1 )
            }

            if( x * 2 <= K && !visited[x * 2]){ // 10 <= 17 && ![17]
                visited[x * 2] = true; // visited[10] = true
                q.add(new int[] { x * 2 , cnt + 1}); // ( 10 , 1 )
            }
        }
    }
}
