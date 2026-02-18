class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        total = 0
        for i in range(ceil(len(nums) / 2)):
            if i == len(nums) - 1 - i:
                total += nums[i]
            else:
                total += int(str(nums[i]) + str(nums[len(nums) - 1 - i]))
                
        return total

        
