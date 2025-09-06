
import java.util.*;

public class Main {
    public static void main(String[] args) {
        List<Integer> arrayLists = new ArrayList<>();
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        for(int i = 0; i < N; i++){
            arrayLists.add(sc.nextInt());
        }
        Collections.sort(arrayLists);

        StringBuilder sb = new StringBuilder();
        for(int arr : arrayLists){
            sb.append(arr);
            sb.append("\n");
        }
        System.out.println(sb.toString());
    }
}
