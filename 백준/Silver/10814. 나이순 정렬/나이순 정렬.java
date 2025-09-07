import java.util.*;

public class Main {
    static final int person_len = 2;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

       // idea help by gpt because i didn't know arrange about 2kinds of type but code is just my self
        // method 1
        List<List<String>> list = new ArrayList<>(201);

        for(int i = 0; i <= 200; i++){
            list.add(new ArrayList<>());
        }

        int N = sc.nextInt();
        for(int i = 0; i < N; i++){
            int age = sc.nextInt();
            String name = sc.next();
            list.get(age).add(name);
        }
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i <= 200; i++){
            for(String name : list.get(i)){
                sb.append(i).append(' ').append(name).append('\n');
            }
        }
        System.out.print(sb.toString());
    }
}