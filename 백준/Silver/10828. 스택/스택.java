import java.util.Scanner;
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        Stack<Integer> stack = new Stack<>();
        StringBuilder sb = new StringBuilder();
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        for(int i = 0; i < N; i++){
            String s = sc.next(); // next로 읽고 nextInt()로 받기 
            if(s.equals("push")){
                int x = sc.nextInt();
                stack.push(x);
            } else if (s.equals("pop")) {
                if(stack.isEmpty()){
                    sb.append(-1);
                    sb.append("\n");
                }else{
                    sb.append(stack.pop());
                    sb.append("\n");
                }
            } else if (s.equals("size")) {
                sb.append(stack.size());
                sb.append("\n");
            } else if (s.equals("empty")) {
                if(stack.isEmpty()){
                    sb.append(1);
                    sb.append("\n");
                }else{
                    sb.append(0);
                    sb.append("\n");
                }
            } else if (s.equals("top")) {
                if(!stack.isEmpty()){
                    sb.append(stack.peek());
                    sb.append("\n");
                }else{
                    sb.append(-1);
                    sb.append("\n");
                }
            }
        }
        System.out.println(sb.toString());
    }
}
