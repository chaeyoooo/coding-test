class Solution {
    public int[] solution(int n) {
        int count = 0;
        
        for(int i = 1 ; i <= n; i++){
            if(i % 2 != 0){
                count++;
            }
        }
        int[] answer = new int[count]; // 5개 칸 배열
        
        int index = 0;
        for(int i = 1 ; i <= n; i++){
            if(i % 2 != 0){
                answer[index] = i;
                index++;
            }
        }
        return answer;
    }
}