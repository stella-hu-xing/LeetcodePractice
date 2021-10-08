#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#
# Given an array, rotate the array to the right by k steps,
# where k is non-negative.
# E.g. Input: nums = [1,2,3,4,5,6,7], k = 3
#      Output: [5,6,7,1,2,3,4]

from typing import List

# @lc code=start


class Solution:

    # solution 1: not working, need fix!
    def rotate1(self, nums: List[int], k: int) -> None:
        length = len(nums)
        newL = [None] * length
        for (i, v) in enumerate(nums):
            index = i + k if i + k < length - 1 else i + k - length
            newL[index] = v
        nums[:] = newL

    # solution 2: list slicing
    def rotate2(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]


# @lc code=end
sol = Solution()
list = [1, 2]
sol.rotate2(list, 3)
print(list)
list2 = [1, 2]
sol.rotate1(list2, 3)
print(list2)
