class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]*len(nums)
        post = [1]*len(nums)
        
        
        for i in range(1,len(nums)):
            pre[i]=pre[i-1]*nums[i-1]
            # prefix=prefix*pre[i]
            # print(i," ",prefix)
        
        postfix=1
        for i in range(len(nums)-2,-1,-1):
            post[i]=post[i+1]*nums[i+1] 
            
        
        # print(pre)aa
        # print(post)
        
        res=[1]*len(nums)
        
        for i in range(0,len(nums)):
            res[i] = pre[i] * post[i]
        
        return res
        