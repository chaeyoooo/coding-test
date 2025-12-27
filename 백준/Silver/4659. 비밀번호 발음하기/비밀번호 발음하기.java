import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 모음 하나를 반드시 포함하여야 한다.
        // 모음 3개 혹은 자음 3개 연속 오면 안됨
        // 같은 글자가 연속적으로 두번 오면 안됨 , ee oo 허용
        Scanner sc = new Scanner(System.in);
        while(true){
            String s = sc.next(); // 문자를 받기

            if(s.equals("end")){
                break;
            }

            // 모음 하나를 포함 여부
            int cnt = 0;
            for(int i = 0; i < s.length(); i++){
                if((s.charAt(i) == 'a' )|| (s.charAt(i) == 'e' )|| (s.charAt(i) =='i') || (s.charAt(i) =='o')|| (s.charAt(i) =='u')){
                    cnt++;
                }
            }
            int vowel = 0;
            int not_vowel = 0;
            boolean isCheck = true;
            // 모음 3개 혹은 자음 3개 연속으로 오면 안된다
            for(int i = 0; i < s.length(); i++){
                if((s.charAt(i) == 'a' )|| (s.charAt(i) == 'e' )|| (s.charAt(i) =='i') || (s.charAt(i) =='o')|| (s.charAt(i) =='u')){
                    vowel++;
                    not_vowel = 0;
                }else{
                    not_vowel++;
                    vowel = 0;
                }

                if(vowel >= 3 || not_vowel >=3){
                    isCheck = false;
                }
            }
            boolean isOk = true;
            // 같은 글자가 연속적으로 두번 오면 안됨 , ee oo 허용
            for(int i = 0; i< s.length() -1; i++){
                if(s.charAt(i) == s.charAt(i+1)){
                    if(s.charAt(i) == 'e' || s.charAt(i) == 'o') {
                        isOk = true;
                    }else{
                        isOk = false;
                    }
                }
            }

            if(cnt >= 1 && isCheck && isOk ){
                System.out.println("<" + s + ">" + " is acceptable.");
            }else{
                System.out.println("<" + s + ">" + " is not acceptable.");
            }
        }
    }
}
