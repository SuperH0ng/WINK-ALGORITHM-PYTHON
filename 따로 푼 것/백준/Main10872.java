import java.io.*;

public class Main10872 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int fac = 1;
        while (N > 1) {
            fac *= N;
            N -= 1;
        }
        System.out.println(fac);
    }
}

