import java.util.Scanner;
class Solution
{
	public static void main(String args[]) throws Exception{
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for(int i = 0 ; i < n; i++){
            int k = sc.nextInt();
            int[] count = new int[101];
            for(int j = 0 ; j < 1000; j++){
                int score = sc.nextInt();
                count[score]++;
            }
            int max= 0;
            int mode = 0;
            for(int s = 0; s <= 100; s++){
                if(count[s] > max){
                    max = count[s];
                    mode = s;
                } else if (count[s] == max) {
                    if(s > mode){
                        mode = s;
                    }
                }
            }
            System.out.println("#" + k + " " + mode);
        }
    }
}