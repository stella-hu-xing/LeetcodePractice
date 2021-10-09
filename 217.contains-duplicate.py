#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#
# Given an integer array nums, return true if any value appears
# at least twice in the array, and return false if every element
# is distinct.

from typing import List

# @lc code=start


class Solution:
    # get hashmap, sort and compare last one
    def containsDuplicate1(self, nums: List[int]) -> bool:
        dd = {}
        for x in nums:
            dd[x] = dd[x] + 1 if x in dd else 1
        newD = dict(sorted(dd.items(), key=lambda item: item[1]))
        lastKey = list(newD.keys())[-1]
        return newD[lastKey] > 1

    # get hashmap, convert to list and filter
    def containsDuplicate2(self, nums: List[int]) -> bool:
        dd = {}
        for x in nums:
            dd[x] = dd[x] + 1 if x in dd else 1
        dups = list(filter(lambda v: v > 1, dd.values()))
        return len(dups) > 0

    # get hashmap, iterate dict
    def containsDuplicate3(self, nums: List[int]) -> bool:
        dd = {}
        for x in nums:
            dd[x] = dd[x] + 1 if x in dd else 1
        flag = False
        for k, v in dd.items():
            if v > 1:
                flag = True
                break  ## break out the loop
        return flag

    # get hashmap, use any built in function
    def containsDuplicate4(self, nums: List[int]) -> bool:
        dd = {}
        for x in nums:
            dd[x] = dd[x] + 1 if x in dd else 1
        return any(v > 1 for v in dd.values())

    # Not use hashmap!!
    def containsDuplicate5(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)


# @lc code=end
sol = Solution()
re = sol.containsDuplicate5([1, 2, 3, 4])
print(re)
