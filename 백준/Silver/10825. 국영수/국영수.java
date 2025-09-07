
import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt(); // 12
        String[][] grade = new String[N][4];

        for(int i = 0; i < N; i++){
            grade[i][0] = sc.next(); // 이름
            grade[i][1] = sc.next(); // 국어
            grade[i][2] = sc.next(); // 영어
            grade[i][3] = sc.next(); // 수학
        }

//        국어 점수가 감소하는 순서로 -> 국어 점수가 작
//        국어 점수가 같으면 영어 점수가 증가하는 순서로
//        국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
//        모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로 (단, 아스키 코드에서 대문자는 소문자보다 작으므로 사전순으로 앞에 온다.)

        Arrays.sort(grade, new Comparator<String[]>() {
            @Override
            public int compare(String[] o1, String[] o2) {
                if(Integer.parseInt(o1[1]) - Integer.parseInt(o2[1]) != 0){
                    return Integer.parseInt(o2[1]) - Integer.parseInt(o1[1]); // 감소 하는 순서
                }
                if ((Integer.parseInt(o1[1]) - Integer.parseInt(o2[1]) == 0) && (Integer.parseInt(o2[2]) - Integer.parseInt(o1[2]) != 0)) {
                    return Integer.parseInt(o1[2]) - Integer.parseInt(o2[2]); // 증가하는 순서

                }if ((Integer.parseInt(o1[1]) - Integer.parseInt(o2[1]) == 0 )&& (Integer.parseInt(o1[2]) - Integer.parseInt(o2[2]) == 0) && (Integer.parseInt(o2[3]) - Integer.parseInt(o1[3])!= 0 )){
                    return Integer.parseInt(o2[3]) - Integer.parseInt(o1[3]); // 감소 하는 순서

                }if(Integer.parseInt(o1[1]) - Integer.parseInt(o2[1]) == 0 && Integer.parseInt(o2[2]) - Integer.parseInt(o1[2]) == 0 && Integer.parseInt(o2[3]) - Integer.parseInt(o1[3]) == 0){
                    return o1[0].compareTo(o2[0]);
                }
                return o1[0].compareTo(o2[0]);
            }
        });

        for(int i = 0; i < N; i++){
            System.out.println(grade[i][0]);
        }
    }
}
