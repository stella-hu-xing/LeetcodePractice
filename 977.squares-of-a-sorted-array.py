#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

# Given an integer array nums sorted in non-decreasing order,
# return an array of the squares of each number sorted in
# non-decreasing order.

# requirements: O(n)

from typing import List

# @lc code=start


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        length = len(nums)
        min = 0
        max = length - 1
        index = length - 1
        l = list(range(length))
        while min <= max:
            if abs(nums[min]) < abs(nums[max]):
                l[index] = nums[max] * nums[max]
                max = max - 1
            else:
                l[index] = nums[min] * nums[min]
                min = min + 1
            index = index - 1
        return l


# @lc code=end
