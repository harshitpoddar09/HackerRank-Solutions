import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        /* Enter your code here. Print output to STDOUT. */
        StringBuilder A1=new StringBuilder(A);
        A1.reverse();
        String Arev=A1.toString();
        if (A.equals(Arev)){
            System.out.println("Yes");
        }
        else{
            System.out.println("No");
        }
        
    }
}
