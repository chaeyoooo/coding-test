
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        Set<String> voca_set = new HashSet<>();
        
        String[] voca_dic = new String[N];
        
        for(int i = 0; i < N; i++){
            voca_dic[i] = sc.next();
            voca_set.add(voca_dic[i]);
        }

        List<String> list = new ArrayList<>(voca_set);

        Collections.sort(list, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                if(o1.length() - o2.length() != 0){
                    return o1.length() - o2.length();
                }else{
                    return o1.compareTo(o2);
                }
            }
        });
        for(int i = 0; i < list.size(); i++){
            System.out.println(list.get(i));
        }
    }
}
