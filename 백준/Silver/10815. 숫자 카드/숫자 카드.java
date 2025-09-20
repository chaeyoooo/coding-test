import java.util.ArrayList;
import java.util.HashSet;
import java.util.Scanner;

// 2중 for문으로 풀어서 시간초과
// hashset -> contains O(1) but arraylist , linkedlist -> contains() O(N)
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        HashSet<Integer> hash = new HashSet<>();
        ArrayList<Integer> answer = new ArrayList<>();
        for(int i = 0; i < N; i++){
            hash.add(sc.nextInt());
        }
        int M = sc.nextInt();
        for(int i = 0; i < M; i++){
            answer.add(sc.nextInt());
        }

        for(int i = 0; i < answer.size(); i++){
            if(hash.contains(answer.get(i))){
                System.out.print("1" + " ");
            }else{
                System.out.print("0" + " ");
            }
        }
    }
}
