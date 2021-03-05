import java.util.*;
import java.io.*;
import java.lang.Math;

class Solution{
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        for(int i=0;i<t;i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            int s = a;
            for(int j=0;j<n;j++){
                double c = Math.pow(2, j);
                int d = b*(int)c;
                s = s+d;
                System.out.print(s+" ");
            }
            System.out.println();
        }
        in.close();
    }
}
