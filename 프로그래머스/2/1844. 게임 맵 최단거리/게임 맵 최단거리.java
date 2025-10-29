import java.util.*;
class Solution {
    int[] dr = {-1 , 1 , 0 , 0};
    int[] dc = {0 , 0 , -1 , 1};
    
    public int solution(int[][] maps) {
        int n = maps.length;
        int m = maps[0].length;
        
        boolean[][] visited = new boolean[n][m]; // 방문 배열 선언
        int[][] dist = new int[n][m]; // 거리 배열 선언
        
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{0,0}); 
        
        visited[0][0] = true;
        dist[0][0] = 1;
        
        while(!q.isEmpty()){
            int[] curr = q.poll();
            int nr = curr[0];
            int nc = curr[1];
            
            if(nr == n-1 && nc == m-1){
                return dist[nr][nc];
            }
            
            for(int i = 0; i < 4; i++){
                int nrr = nr + dr[i];
                int ncc = nc + dc[i];
                
                if(nrr < 0 || ncc < 0 || nrr >= n|| ncc >= m) continue;
                if(maps[nrr][ncc] == 0) continue;
                if(visited[nrr][ncc]) continue;
                
                visited[nrr][ncc] = true;
                dist[nrr][ncc] = dist[nr][nc] + 1;
                q.add(new int[] {nrr , ncc});
            }
        }
        return -1;
    }
}