class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # major, val = 0, 0
        # for i in set(nums):
        #     c = nums.count(i)
        #     if c > major: major, val = c, i
        # return val
        nums.sort()
        mid = len(nums) // 2
        return nums[mid]
                
