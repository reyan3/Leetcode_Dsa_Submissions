class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r,w,b = 0,0,0
        
        # take all frequencies
        for i in range(len(nums)):
            if nums[i]==0:
                r+=1
            elif nums[i]==1:
                w+=1
            else:
                b+=1

        # now subtract frequency of r,w,b until 0
        idx = 0
        while r>0:
            nums[idx] = 0
            idx+=1
            r-=1
        while w>0:
            nums[idx] = 1
            idx+=1
            w-=1
        while b>0:
            nums[idx] = 2
            idx+=1
            b-=1
        