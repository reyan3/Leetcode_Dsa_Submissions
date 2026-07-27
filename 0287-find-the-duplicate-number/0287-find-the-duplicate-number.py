class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow,fast = nums[0] , nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast: #if cycle found
                break
            
        slow = nums[0] # reinitialize slow to start and continue till slow == fast
        
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow