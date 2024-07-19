package Java;

import java.util.HashSet;
import java.util.Set;

public class LC_3 {
    public static void main(String[] args) {

        String s = "abcabcbb";
        // System.out.println(s); 
        int maxans = Integer.MIN_VALUE;
        // System.out.println(maxans);
        Set<Character> chars= new HashSet<Character>(); 

        Integer l=0;

        for (int r=0;r<=s.length()-1;r++){
            while(l< r && chars.contains(s.charAt(r))){
                chars.remove(s.charAt(r));
                l++;
            }

            chars.add(s.charAt(r));
            maxans= Math.max(maxans, r-l+1);

        }

        System.out.println(maxans);
    }
}
