#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z'],
        }
        if len(digits)==0: return []
        if len(digits)==1: 
            return dict[digits]
        else:
            # l = list(map(lambda x: [x+i for i in dict[digits[0]]], self.letterCombinations(digits[1:])) )
            return [x+i for i in dict[digits[0]] for x in self.letterCombinations(digits[1:])]


sol = Solution()
print(sol.letterCombinations('62')    )
  
# @lc code=end

