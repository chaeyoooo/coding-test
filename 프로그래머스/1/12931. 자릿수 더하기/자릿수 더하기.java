import java.util.*;

public class Solution {
    public int solution(int n) {
        // n을 char로 바꿔야됨
        String s = Integer.toString(n);
        int answer = 0;
        for(int i = 0; i < s.length(); i++){
            answer += s.charAt(i) - '0';
        }
        return answer;
    }
}