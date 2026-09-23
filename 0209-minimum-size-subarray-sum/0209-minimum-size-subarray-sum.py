class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l = 0 
        sum = 0
        minl = float("inf")

        for r in range(len(nums)):
            sum+=nums[r]
            # sum until sum is > or == target
            while sum>=target:
                # run loop till sum >= target and check length
                minl = min(minl , r-l+1)
                # decrease from left till sum >= target
                sum-=nums[l]
                l+=1
        
        return minl if minl != float("inf") else 0 
