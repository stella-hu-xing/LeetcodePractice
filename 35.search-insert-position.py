#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#
from typing import List

# @lc code=start


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        min = 0
        max = len(nums) - 1
        while min <= max:
            pivot = min + round((max - min) / 2)
            if nums[pivot] == target:
                return pivot
            if nums[pivot] < target:
                min = pivot + 1
            if nums[pivot] > target:
                max = pivot - 1
        return min


# @lc code=end
sol = Solution()
print(sol.searchInsert([1, 3, 5, 6], 7))
