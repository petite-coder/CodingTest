import java.io.*;
import java.util.*;

public class Main {
    static int[][] dp = new int[30][30];

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int t = Integer.parseInt(br.readLine());
        for(int i=1; i<=t; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int west = Integer.parseInt(st.nextToken());
            int east = Integer.parseInt(st.nextToken());

            // mCn
            bw.write(combi(east, west)+"");
            bw.newLine();
        }

        bw.flush();
        bw.close();
        br.close();
    }

    static int combi(int m, int n) {
        if(dp[m][n] > 0) {
            return dp[m][n];
        }

        if(m == n || n ==0) {
            return dp[m][n] = 1;
        }

        return dp[m][n] = combi(m-1, n-1) + combi(m-1, n);
    }

}