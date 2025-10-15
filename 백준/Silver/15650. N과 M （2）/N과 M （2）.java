import java.util.Arrays;
import java.util.Scanner;

public class Main {
	static int arr_num;
	static int choice_num;
	static int[] choice;
	static int[] arr;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		arr_num = sc.nextInt(); // 4 
		choice_num = sc.nextInt(); // 2
		
		// 먼저 arr을 배열로 바꾸기
		arr = new int[arr_num];
		for(int i = 0; i < arr_num; i++) {
			arr[i] = i+1; // 1 2 3 4 
		}
		
		choice = new int[choice_num];
		
		combination(0,0);
	}

	private static void combination(int arrIndex, int findIndex) {
		// 종료 조건
		StringBuilder sb = new StringBuilder();
		if(findIndex == choice_num) {
			for(int i = 0; i < choice_num; i++) {
				System.out.print(choice[i] + " ");
			}
			System.out.println();
			return;
		}
		
		for(int i = arrIndex; i <= arr_num - choice_num + findIndex; i++) {
			choice[findIndex] = arr[i];
			
			combination(i+1 , findIndex+ 1);
		}
	}
}
