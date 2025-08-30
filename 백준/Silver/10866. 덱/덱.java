
import java.util.Deque;
import java.util.LinkedList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();
        sc.nextLine();

//        push_front X: 정수 X를 덱의 앞에 넣는다.
//        push_back X: 정수 X를 덱의 뒤에 넣는다.
//        pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
//        pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
//        size: 덱에 들어있는 정수의 개수를 출력한다.
//        empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
//        front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
//        back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.

        Deque<Integer> deque = new LinkedList<>();
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < T; i++){
            String result = sc.nextLine();
            String[] part = result.split(" ");
            String cmd = part[0];

            if(cmd.equals("push_front")){
                int x = Integer.parseInt(part[1]);
                deque.addFirst(x);
            } else if (cmd.equals("push_back")) {
                int x = Integer.parseInt(part[1]);
                deque.addLast(x);
                
            } else if(result.equals("pop_front")){
                if(!deque.isEmpty()){
                    sb.append(deque.removeFirst());
                    sb.append("\n");
                }else{
                    sb.append("-1");
                    sb.append("\n");
                }
            }else if (result.equals("pop_back")){
                if(!deque.isEmpty()){
                    sb.append(deque.removeLast());
                    sb.append("\n");
                }else{
                    sb.append("-1");
                    sb.append("\n");
                }
            }else if (result.equals("size")) {
                sb.append(deque.size());
                sb.append("\n");
            }else if (result.equals("empty")) {
                if(deque.isEmpty()){
                    sb.append("1");
                    sb.append("\n");
                }else{
                    sb.append("0");
                    sb.append("\n");
                }
            }else if (result.equals("front")) {
                if(!deque.isEmpty()){
                    sb.append(deque.getFirst());
                    sb.append("\n");
                }else{
                    sb.append("-1");
                    sb.append("\n");
                }
            }else if (result.equals("back")) {
                if (!deque.isEmpty()) {
                    sb.append(deque.getLast());
                    sb.append("\n");
                } else {
                    sb.append("-1");
                    sb.append("\n");
                }
            }
        }
        System.out.println(sb.toString());
    }
}
