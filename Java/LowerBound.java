package Java;

public class LowerBound {
    public static int lowerBound(int []arr, int n, int x) {
        // Write your code here
        Integer l=0;
        Integer h=n-1;
        Integer res = n;
        Integer mid=0;

        while(l<=h){
            mid=(l+h)/2;

            if(arr[mid]>=x){
                res=mid;
                h=mid-1;

            }   
            else
            {
                l=mid+1;
            } 

        }

        return res;

    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 8, 10, 11, 12, 19};
        int n = arr.length;
        int x = 5;
        
        int result = lowerBound(arr, n, x);
        System.out.println("The lower bound index of " + x + " is: " + result);
    }
}
