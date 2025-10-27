class Solution {
    public int[] solution(String s) {
        int rotate = 0;      
        int removed = 0;   
        
        
        while(!s.equals("1")){
            String[] s_arr = s.split("");
            int cnt = 0;
        
 
        for(String ss : s_arr){
            if(Integer.parseInt(ss) == 1){
                cnt++;
            }else{
                removed++;
            }
        }
        s = Integer.toBinaryString(cnt);
        rotate++;
    }
        int[] answer = {rotate, removed};
        return answer;
}
}