import java.io.*;
import java.util.StringTokenizer;

public class Main1712 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer nums = new StringTokenizer(br.readLine());
        double A = Integer.parseInt(nums.nextToken());
        int B = Integer.parseInt(nums.nextToken());
        int C = Integer.parseInt(nums.nextToken());

        if (B >= C) {
            System.out.println(-1);
        } else {
            System.out.println((int) Math.ceil((A + 1) / (C - B)));
        }
    }
}
