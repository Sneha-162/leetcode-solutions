class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        bound = 0
        count = 0
        for i in range(len(nums)):
            bound += nums[i]
            if bound == 0:
                count += 1
        return count

        
