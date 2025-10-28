class Solution{
    String[] vowels = {"A" , "E" , "I" , "O" , "U"};
    int count = 0;
    int answer = 0;
    String target;
    
    public int solution (String word){
        target = word;
        dfs("");
        return answer;
    }
    
    void dfs(String cur){
        if(!cur.equals("")){
            count++;
            
            if(cur.equals(target)){
                answer = count;
                return;
            }
        }
    
        if(cur.length() == 5) return;
    
        for(int i = 0; i < 5; i++){
            dfs(cur + vowels[i]);
            if(answer != 0) return;
        }
    }
}
