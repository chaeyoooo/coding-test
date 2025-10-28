import java.util.*;
class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        // 먼저 돌아라 commands를
        for(int i = 0; i < commands.length; i++){
            // 2부터 5까지 돌아라 
            // 저장할 배열 만들어두기 sub_arr 가 저장이 잘 안되는 문제 발생 
                int[] sub_arr = new int[commands[i][1] - commands[i][0] + 1]; 
            for(int j = commands[i][0] -1 , k = 0; j <= commands[i][1] -1 ; j++ , k++){ 
                sub_arr[k] = array[j];
            }
             Arrays.sort(sub_arr);
            answer[i] = sub_arr[commands[i][2]-1];
        }
        return answer;
    }
}