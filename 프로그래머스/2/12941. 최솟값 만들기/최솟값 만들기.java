import java.util.*;
class Solution
{
    public int solution(int []A, int []B)
    {
        int answer = 0;
        // 먼저 A를 정렬하자 , B는 반대로 정렬하자
        Arrays.sort(A); // 1 2 4 
        Arrays.sort(B); // 5 4 4
        
        for(int i = 0; i < B.length / 2; i++){
            int temp = B[i]; // temp = B[O] = 5
            B[i] = B[B.length - 1 - i]; // B[0] = B[3-1-0] , 5 = 4
            B[B.length -1 - i] = temp; // B[2] = B[0] , 4 = 5
        }
        
        for(int i = 0; i < A.length; i++){
            answer += A[i] * B[i];
        }
    
        return answer;
    }
}