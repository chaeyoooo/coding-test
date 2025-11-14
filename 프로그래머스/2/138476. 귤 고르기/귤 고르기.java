import java.util.*;
class Solution {
    public int solution(int k, int[] tangerine) {
        Map<Integer, Integer> map = new HashMap<>();
        for(int x : tangerine){
            // 귤을 돌면서
            map.put(x, map.getOrDefault(x,0) + 1);
        }
        
        // 개수만 리스트로 만들어서
        List<Integer> list = new ArrayList<>(map.values());
        
        // 내림 차순 정렬
        Collections.sort(list , Collections.reverseOrder());
        
        int kinds = 0;
        for(int cnt : list){
            k-= cnt;
            kinds++;
            
            if(k <= 0) break;
        }
        return kinds;
    }
}