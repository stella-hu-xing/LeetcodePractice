#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#
from typing import List

# @lc code=start


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = 0
        left = 0
        right = len(nums) - 1
        while left <= right:
            pivot = left + round((right - left) / 2)  # this is the point
            if nums[pivot] == target:
                return pivot
            if nums[pivot] > target:
                right = pivot - 1
            if nums[pivot] < target:
                left = pivot + 1
        return -1


# @lc code=end
sol = Solution()
re = sol.search([-1, 0, 3, 5, 9, 12], 9)
print(re)
