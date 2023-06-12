class Solution:
    def __recpermute(nums,freq,ds,ans):
        n=len(nums)
        if len(ds)==n:
            ans.append(ds.copy())
            return
        
        for i in range(n):
            if(freq[i]==0): 
                freq[i]=1
                ds.append(nums[i])
                Solution.__recpermute(nums,freq,ds,ans)
                ds.pop()
                freq[i]=0
    def permute(self, nums: list[int]) -> list[list[int]]:
        import numpy as np
        n=len(nums)
        freq=np.zeros(n,int)
        ds=[]
        ans=[]
        Solution.__recpermute(nums,freq,ds,ans)
        return ans  

print(Solution().permute([1,2,3]))