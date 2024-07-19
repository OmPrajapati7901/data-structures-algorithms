package Java;

import java.util.HashSet;

public class LC_217 {
    public static void main(String[] args) {

        int[] num = {1,2,3,1};
        // System.out.println(num[1]);
        HashSet<Integer> set = new HashSet<Integer>();

        for (int i=0;i<num.length;i++){
            if (set.contains(num[i])) {
                System.out.println("duplicate");
                // return true;
            }

            set.add(num[i]);

        }


    }
}
