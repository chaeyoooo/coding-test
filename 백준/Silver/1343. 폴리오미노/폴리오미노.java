import java.util.Scanner;

public class Main{

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // XX.XXXXXXXXXX..XXXXXXXX...XXXXXX

        String s = sc.next();
        if(!checked(s)){
            System.out.println(-1);
            return;
        }

        s = s.replace("XXXX" ,"AAAA");
        s = s.replace("XX","BB");

        System.out.println(s);
    }

    private static boolean checked(String s){
        // 기억해야할점 -> .은 모든 문자를 의미하기에 기준이 될 수 없음 . 정규식 이스케이프가 필요
        String[] stringSplit = s.split("\\.");

        for(int i = 0; i < stringSplit.length; i++){
            // 예를들어 10인경우를 생각해보자
            // 10 / 4 -> 2 가되니까 이는 aaaa가 2번 나머지는 2니까 2 % 2 == 0
            // 2, 4, 6, 8 , 10 , 12 , 14 ,
             if (stringSplit[i].length() % 2 != 0) {
                // 홀수인 경우
                return false;
            }
        }
        return true;
    }
}
