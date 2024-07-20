// 34. Find First and Last Position of Element in Sorted Array


package Java;


public class LC_34 {
    public static int lB(int[] arr, int n, int x) {

        int l = 0;
        int h = n - 1;
        int res = n;
        int mid = 0;

        while (l <= h) {
            mid = (l + h) / 2;

            if (arr[mid] >= x) {
                res = mid;
                h = mid - 1;
            } else {
                l = mid + 1;
            }
        }

        return res;
    }

    public static int uB(int[] arr, int n, int x) {

        int l = 0;
        int h = n - 1;
        int res = n;
        int mid = 0;

        while (l <= h) {
            mid = (l + h) / 2;

            if (arr[mid] > x) {
                res = mid;
                h = mid - 1;
            } else {
                l = mid + 1;
            }
        }

        return res;
    }

    public static void main(String[] args) {
        // int[] arr = {1, 2, 8, 10, 11, 12, 19};
        int[] nums = { 5, 7, 7, 8, 8, 10 };
        int n = nums.length;
        int target = 8;

        int l_result = lB(nums, n, target);
        // if (l_result == -1) 
        int u_result = uB(nums, n, target);


        if(l_result==n || nums[l_result]!=target) {
                System.out.println("{-1,-1}");
        // return new int[] {-1,-1};
        }

        // return new int[] {l_result,u_result-1};
        System.out.println("The lower bound index of " + target + " is: " + l_result);
        System.out.println("The upper bound index of " + target + " is: " + u_result);
    }

}
