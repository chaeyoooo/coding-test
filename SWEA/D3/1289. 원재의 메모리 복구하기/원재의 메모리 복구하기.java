

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.Scanner;

public class Solution {
    public static void main(String[] args)  {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt(); // testcase 입력받기
        for (int testcase = 1; testcase <= T; testcase++) {

            // 메모리 두개 입력받기
            String s = sc.next();
            // string -> split해서 자르기 !
            String[] s_array = s.split("");

            int[] i_array = new int[s_array.length];

            for (int j = 0; j < i_array.length; j++) {
                i_array[j] = Integer.parseInt(s_array[j]);
            }

            int count = 0;
            boolean isCheck = false;
            for (int k = 0; k < i_array.length; k++) {
                if (i_array[k] == 1) {
                    for (int l = k; l < i_array.length; l++) {
                        if(i_array[l] == 0){
                            i_array[l] = i_array[l] + 1;
                        }else{
                            i_array[l] = i_array[l] - 1;
                        }
                    }
                    count++;
                }
            }
           System.out.println("#" + testcase + " " + count);
        }
    }
}

