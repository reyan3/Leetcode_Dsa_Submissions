class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = nums[0]
        sum = 0


        for i in range(len(nums)):
            sum+=nums[i]

            maxi = max(maxi , sum)

            if sum < 0:
                sum = 0
        
        return maxi