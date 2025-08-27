
import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt(); // 테스트 케이스 개수
        while(T-- > 0){
            // 큐
            Queue<int[]> queue = new LinkedList<>();

            //우선순위 큐
            PriorityQueue<Integer> priorityQueue = new PriorityQueue<>(Comparator.reverseOrder()); // 기본값이 최소힙이므로 , 최대 힙으로 변경

            int N = sc.nextInt(); // 문서의 갯수
            int M = sc.nextInt(); // 몇번째로 인쇄 되었는지 인덱스 번호

            for(int i = 0; i < N; i++){
                int importance = sc.nextInt();
                queue.offer(new int[]{i , importance}); // 인덱스 , 중요도
                priorityQueue.offer(importance); // 우선순위 큐에 중요도 삽입
            }

            // 정답변수
            int count = 0;
            // 큐가 비지 않았을 떄까지
            while(!queue.isEmpty()){
                int[] current_queue = queue.poll(); // queue에서 하나씩 제거
                // 중요도 같으면
                if(current_queue[1] == priorityQueue.peek()){
                    priorityQueue.poll(); // 왜 여기서 삭제를 해야하는지 ?
                    count++;

                    //인덱스 같으면
                    if(current_queue[0] == M){
                        System.out.println(count);
                        break;
                    }

                // 중요도 다르면 뒤로 밀기
                }else{
                    queue.offer(current_queue); // 뒤로 이동
                }
            }
        }
    }
}
