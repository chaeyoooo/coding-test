import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt(); // 15 , 자연수 넣기

        // 변수 초기화
        int sum = 1; // startindex와 endindex의 합 -> 1부터 1까지의 합
        int count = 1; // 갯수 (마지막 15를 포함)
        int startindex = 1; // 인덱스 1
        int end_index = 1; // 인덱스 1

        // end_index가 15가 아닐때까지
        while(end_index != N){
            // 합이 15를 넘으면
            if(sum > N){
                sum = sum - startindex;
                startindex++;
            } else if (sum < N) {
                end_index++;
                sum = sum + end_index;          
            } else if (sum == N) { // 왜 startindex는 증가 안시키고 ?
                end_index++;
                sum = sum + end_index;
                count++;
            }
        }
        System.out.println(count);
    }
}
