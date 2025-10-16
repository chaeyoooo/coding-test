import java.util.Scanner;
import java.util.Stack;

public class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();
        for(int i = 0; i < T; i++){
            Stack<String> stack = new Stack<>();
            // 테스트 케이스 반복해라
            String[] s = sc.next().split("");

            for (int j = 0; j < s.length; j++) {
                String cur = s[j];
                if (cur.equals("(")) {
                    stack.push(cur);
                } else {
                    if (!stack.isEmpty()) {
                        if(stack.peek().equals("(")){
                            stack.pop();
                        }
                    } else {
                        stack.push(")");
                    }
                }
            }
            if(stack.isEmpty()){
                System.out.println("YES");
            }else{
                System.out.println("NO");
            }
        }
    }
}
