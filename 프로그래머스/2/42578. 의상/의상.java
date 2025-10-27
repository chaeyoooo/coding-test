import java.util.*;
class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        
        // 1. 종류 별로 옷 개수를 세기 위한 HashMap 생성
        Map<String , Integer> map = new HashMap<>();
        
        for(int i = 0; i < clothes.length; i++){
            String type = clothes[i][1];
            map.put(type , map.getOrDefault(type , 0) + 1);
        }
        
        for(int count : map.values()){
            answer *= (count + 1);
        }

        return answer -1;
    }
}