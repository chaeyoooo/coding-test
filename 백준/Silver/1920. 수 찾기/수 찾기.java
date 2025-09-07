
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] arr1 = new int[N];
        for(int i = 0; i < arr1.length; i++){
            arr1[i] = sc.nextInt();
        }

        int M = sc.nextInt();
        int[] arr2 = new int[M];
        for(int i = 0; i < arr2.length; i++){
            arr2[i] = sc.nextInt();
        }
        Arrays.sort(arr1);
//        Arrays.sort(arr2);

        for(int i = 0; i < arr2.length; i++){

            int result = binarySearch(arr1, arr2[i]);
/*            System.out.println(result);*/
            if(result == -1){
                System.out.println(0);
            }else{
                System.out.println(1);
            }
        }
    }

    public static int binarySearch(int[] arr , int key){
        int start  = 0;
        int end = arr.length -1;

        while(start <= end){
            int mid = (start + end) / 2;

            if(key < arr[mid]){
                end = mid -1;
            } else if (key > arr[mid]) {
                start = mid + 1;
            }else{
                return mid;
            }
        }
        return -1;
    }
}
