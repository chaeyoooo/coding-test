class Solution {
    public String solution(int age) {
        // abcdefghij
        // age를 char로 만들고 
        // 만약 이게 1이라면 "a"
        String answer = "";
        String age_new = String.valueOf(age);
        char[] age_char = age_new.toCharArray();
        // age_char돌면서 '0'부터 '9까지'체크하기
        for(int i = 0; i < age_char.length; i++){
            if(age_char[i] == '0'){
                answer += "a";
            }else if(age_char[i] == '1'){
                answer +="b";
            }else if(age_char[i] == '2'){
                answer +="c";
            }else if(age_char[i] == '3'){
                answer +="d";
            }else if(age_char[i] == '4'){
                answer +="e";
            }else if(age_char[i] == '5'){
                answer +="f";
            }else if(age_char[i] == '6'){
                answer +="g";
            }else if(age_char[i] == '7'){
                answer +="h";
            }else if(age_char[i] == '8'){
                answer +="i";
            }else if(age_char[i] == '9'){
                answer +="j";
            }
        }
        
        
        return answer;
    }
}