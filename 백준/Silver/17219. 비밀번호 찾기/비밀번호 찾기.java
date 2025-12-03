import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.StringTokenizer;

// 2차원 배열 -> 시간 초과 ... omg
// map 으로 풀자 !
public class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        Map<String , String> map = new HashMap<>();

        int N = sc.nextInt();
        int M = sc.nextInt();

        for(int i = 0; i < N; i++){
            String link = sc.next();
            String pw = sc.next();

            map.put(link , pw);
        }

        for(int i = 0; i < M; i++){
            String s = sc.next();
            System.out.println(map.get(s));
        }
    }
}
