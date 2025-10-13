// 점점 감 잡고 있음
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    static int[] arr;
    static boolean[] visited;
    static int[] answer = new int[6];
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while(true){
            int k = sc.nextInt();
            if(k == 0) break;

            arr = new int[k];
            visited = new boolean[k];
            for(int i = 0; i < k; i++){
                arr[i] = sc.nextInt();
            }
            dfs(0,0);
            System.out.println();
        }
    }
    static void dfs(int start, int count){
        if(count == 6){
            for(int i = 0; i < 6; i++){
                System.out.print (answer[i] + " ");
            }
            System.out.println();
            return;
        }

        // 여기에 dfs로직
        for(int i = start; i < arr.length; i++){
            if(!visited[i]){
                visited[i] = true; // 방문처리
                // 여기서 배열을 넣어야할듯
                answer[count] = arr[i];
                dfs(i + 1, count + 1);
                visited[i] = false;
            }
        }
    }
}
