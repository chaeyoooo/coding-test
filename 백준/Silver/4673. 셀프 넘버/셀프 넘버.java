
public class Main {
    // 그 숫자  + 각 자리의 수 의 합

    public static void main(String[] args) {
        boolean[] checked = new boolean[10001];
        for(int i = 1; i <= 10000; i++){
            int n = Checked(i);
            if(n <= 10000){
                checked[n] = true;
            }
        }

        for(int i = 1; i <= 10000; i++){
            if(!checked[i]){
                System.out.println(i);
            }
        }
    }

    public static int Checked(int number){
        String[] s = String.valueOf(number).split("");

        int middle = 0;
        for(int i = 0; i < s.length; i++){
            middle += Integer.parseInt(s[i]) ;
        }
        return middle + number;
    }
}
