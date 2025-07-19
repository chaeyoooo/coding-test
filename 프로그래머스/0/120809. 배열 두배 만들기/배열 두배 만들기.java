class Solution {
    public int[] solution(int[] numbers) {
        int[] array = new int[numbers.length];
        for(int i = 0; i < numbers.length; i++){
            array[i] = numbers[i]  * 2;
        }
        return array;
    }
}