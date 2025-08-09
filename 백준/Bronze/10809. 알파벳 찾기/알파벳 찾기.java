

import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        char[] chars = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
        String strings = sc.next(); //baekjoon

        int[] charsarray = new int[chars.length];

        for(int i = 0; i < chars.length; i++){
            charsarray[i] = strings.indexOf(chars[i]);
        }
        for(int j = 0; j < charsarray.length; j++){
            System.out.print(charsarray[j] + " ");
        }
    }
}
