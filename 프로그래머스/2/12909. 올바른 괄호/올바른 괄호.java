import java.util.*;
class Solution {
    boolean solution(String s) {
        boolean answer = true;

        // ( 이게 나오면 stack에 넣어라
        // ) 이게 나오면 stack이 비어있지 않으면 pop해라 
        // 만약 stack확인했을 때 비어있으면 true 아니면 false를 출력해라 
        
        // 스택을 선언하자
        Stack<String> stack = new Stack<>();
        
        // 2. split으로 나눠서 string배열에 넣어라
        String[] s_arr = s.split("");
        for(int i = 0; i < s_arr.length; i++){
            if(s_arr[i].equals("(")){
                stack.push(s_arr[i]); 
            }else{
                if (stack.isEmpty()) {
                    return false;
                } else {
                     stack.pop();
                }
            }
        }
        
        if(stack.isEmpty()){
            answer = true;
        }else{
            answer = false;
        }
        return answer;
    }
}