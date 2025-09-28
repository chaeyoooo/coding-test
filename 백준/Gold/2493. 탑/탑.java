import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine()); // 갯수

        int[] answer = new int[N];
        Stack<int[]> stack = new Stack<>();

        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < N; i++){
            int height = Integer.parseInt(st.nextToken());
            int index = i +1;

            while(!stack.isEmpty() && stack.peek()[1] <= height){
                stack.pop();
            }

            if(stack.isEmpty()) answer[i] = 0;
            else answer[i] = stack.peek()[0];

            stack.push(new int[]{index , height});
        }
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i <N; i++){
            sb.append(answer[i]).append(" ");
        }
        System.out.println(sb);
    }
}
