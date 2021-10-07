#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

## Binary Search


class Solution:
    def firstBadVersion(self, n):
        min = 1
        max = n
        while min < max:
            pivot = min + round((max - min) / 2)
            if isBadVersion(pivot) == False:
                min = pivot + 1
            if isBadVersion(pivot) == True:
                max = pivot
        return min


# @lc code=end
