import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    static int N;
    static boolean[] viisted;
    static int[][] arr;
    static List<int[]> teamList = new ArrayList<>();
    static int[] picked;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        arr = new int[N][N];
        viisted = new boolean[N];
        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                arr[i][j] = sc.nextInt();
            }
        }
        picked = new int[N/2];// 뽑은 리스트
        
        dfs(0, 0, picked);
        int min = Integer.MAX_VALUE;
        // 인덱스 계산
        for (int[] teamA : teamList) {
            boolean[] checked = new boolean[N]; // N안에 A값 들어있는지 체크
            for (int i : teamA) {
                checked[i] = true; // 팀A가 있는지 체크함
            }
            List<Integer> teamB = new ArrayList<>();
            for(int i = 0; i < N; i++){
                if(!checked[i]){ // 팀 A에 포함되어 있지 않는다면
                    teamB.add(i);
                }
            }
            // 최솟값 보기
            int teamA_sum = 0;
            int teamB_sum = 0;
            for (int x = 0; x < N; x++) {
                for (int y = 0; y < N; y++) {
                    if (checked[x] && checked[y]) teamA_sum += arr[x][y];
                    if (!checked[x] && !checked[y]) teamB_sum += arr[x][y];
                }
            }
            min = Math.min(min, Math.abs(teamA_sum - teamB_sum));
        }
        System.out.println(min);
    }
    // 여기서 인덱스 번호를 뽑고 메인에서 처리 하게 끔 조합을 만들기 위해서
    static void dfs(int depth , int start,  int[] picked){
        if(depth == N /2){
            //로직 넣기
            teamList.add(picked.clone());
            return;
        }
        for(int i = start; i < N; i++){
            if(!viisted[i]){
                viisted[i] = true;
                picked[depth] = i;
                dfs(depth + 1, i+ 1, picked);
                viisted[i] = false;
            }
        }
    }
}
