class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = 0
        for i in range(0, len(nums)):
            comp = target - nums[i] 
            if comp in nums:
                 ind = nums.index(comp)
                 if ind != i: return sorted([i, ind])
