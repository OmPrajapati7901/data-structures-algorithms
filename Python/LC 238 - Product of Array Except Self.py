from typing import List

class Solution:
    # Approach 1: Using Prefix and Postfix Arrays
    def productExceptSelf_approach1(self, nums: List[int]) -> List[int]:
        # Initialize prefix and postfix arrays with 1s
        pre = [1] * len(nums)
        post = [1] * len(nums)

        # Compute prefix products
        for i in range(1, len(nums)):
            pre[i] = pre[i - 1] * nums[i - 1]

        # Compute postfix products
        for i in range(len(nums) - 2, -1, -1):
            post[i] = post[i + 1] * nums[i + 1]

        # Compute result array by multiplying prefix and postfix products
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = pre[i] * post[i]

        return res

    # Approach 2: Using a Single Pass with a Postfix Variable
    def productExceptSelf_approach2(self, nums: List[int]) -> List[int]:
        # Initialize the result array with 1s
        res = [1] * len(nums)

        # Compute prefix products directly into the result array
        for i in range(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]

        # Compute postfix products and multiply directly into the result array
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res

# Test the function with the provided input
nums = [1, 2, 3, 4]
solution = Solution()
print("Approach 1:", solution.productExceptSelf_approach1(nums))
print("Approach 2:", solution.productExceptSelf_approach2(nums))
