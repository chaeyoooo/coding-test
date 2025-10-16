
import java.util.Scanner;
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while(true){
            Stack<String> stack = new Stack<>();
            String s = sc.nextLine();
            if(s.equals(".")){
                break;
            }

            String[] strings = s.split("");
            boolean ischecked = true;
            for(int i = 0; i < strings.length; i++){
                String cur = strings[i];


                // ( 인 경우
                if(cur.equals("(")){
                    stack.push("(");
                }else if(cur.equals(")")){
                    if(stack.isEmpty() || !stack.peek().equals("(")){
                        ischecked = false;
                        break;
                    }else{
                        stack.pop();
                    }

                    // [ 인경우
                }else if(strings[i].equals("[")) {
                    stack.push("[");
                }else if(strings[i].equals("]")){
                    if(stack.isEmpty() || !stack.peek().equals("[")){
                        ischecked = false;
                        break;
                    }else{
                        stack.pop();
                    }
                }
            }
            if(stack.isEmpty() && ischecked){
                System.out.println("yes");
            }else{
                System.out.println("no");
            }
        }
    }
}
