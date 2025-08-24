class Solution {
    public int solution(int num, int k) {
        // num에서 k를 찾고 index를 리턴해라
        // 근데 int -> string으로 만들어야 함
        String num_new = Integer.toString(num);
        char [] s = num_new.toCharArray();
        int result = -1;
        for(int i = 0; i < s.length; i++){
            if(s[i] == (char)(k + '0')){
                result = i + 1;
                break;
            }
        }

        return result;
    }
}