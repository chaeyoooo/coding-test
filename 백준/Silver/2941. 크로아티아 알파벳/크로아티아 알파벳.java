

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String[] dic = {"c=" , "c-" , "dz=" , "d-" , "lj" , "nj" , "s=" , "z="};

        String s = sc.next();

        for(int i = 0; i < dic.length; i++){
            if(s.contains(dic[i])){
                s = s.replace(dic[i],"#");
            }
        }
        System.out.println(s.length());
    }
}
