/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 10818                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: gcy9293 <boj.kr/u/gcy9293>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/10818                          #+#        #+#      #+#    */
/*   Solved: 2025/08/08 23:39:34 by gcy9293       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int[] arr = new int[n];

        for(int i = 0; i < n; i++){
            arr[i] = sc.nextInt();
        }

        int max = arr[0];
        int min = arr[0];

        for(int i = 1; i < n; i++){
            if(max < arr[i]){
                max = arr[i];
            }
            if(min > arr[i]){
                min = arr[i];
            }
        }

        System.out.print(min + " " + max);
    }
}