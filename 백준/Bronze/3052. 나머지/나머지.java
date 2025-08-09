import java.util.HashSet;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in); // scanner 받기
        HashSet<Integer> set = new HashSet(); // 해시 셋

        int[] arr = new int[10];

        for(int i = 0; i < arr.length; i++){
            arr[i] = sc.nextInt();
        }

        for(int i = 0; i < arr.length; i++){
            int count = arr[i] % 42;
            set.add(count);
        }
        System.out.println(set.size());
    }
}
