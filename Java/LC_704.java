package Java;

public class LC_704 {
    public static void main(String[] args) {
        Integer[] nums = {-1,0,3,5,9,12};
        Integer target = 9;

        Integer l=0;
        Integer h = nums.length-1;

        Integer mid =0;
        while (l<=h){
            mid=(l+h)/2;

            if (nums[mid]==target){
                System.out.println(mid);
                break;
                // return mid
            }

            if (target<nums[mid]){
                h=mid-1;

            }
            if (target>nums[mid]){
                l=mid+1;
                
            }
            
            
        }


        System.out.println("-1");
        //  System.out.println(nums.length);

    }
}
