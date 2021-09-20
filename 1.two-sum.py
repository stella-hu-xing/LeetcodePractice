#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        copy = nums.copy()
        for i,v in enumerate(nums):
            copy.remove(v)
            if target-v in copy:
                return [i, i+1+copy.index(target-v)]

        
# @lc code=end

