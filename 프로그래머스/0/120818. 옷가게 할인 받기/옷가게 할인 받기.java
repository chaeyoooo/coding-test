class Solution {
    public int solution(int price) {
        int result = 0;
        if(price >= 500000){
            result = price * 80 /100;
        }else if(price >= 300000){
            result = price * 90 / 100;
        }else if(price >= 100000){
            result = price * 95 /100;
        }else{
            result = price;
        }
        return result;
    }
}