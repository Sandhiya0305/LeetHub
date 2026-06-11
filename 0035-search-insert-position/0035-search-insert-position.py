class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        f, l = 0, len(nums) - 1
        while f <= l:
            mid = (f + l) // 2
            if nums[mid] == target: return mid
            elif nums[mid] > target: l = mid - 1
            else: f = mid + 1
        return f
