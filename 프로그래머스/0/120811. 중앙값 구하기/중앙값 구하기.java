import java.util.Arrays;
class Solution {
    public int solution(int[] array) {
        // 중앙에 위치 하는 값 
        // 1 , 2 , 7 , 10 , 11 -> 중앙값 7
        Arrays.sort(array);
        int n = array.length / 2;
        return array[n];
    }
}