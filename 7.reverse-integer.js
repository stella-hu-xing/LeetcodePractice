/*
 * @lc app=leetcode id=7 lang=javascript
 *
 * [7] Reverse Integer
 *
 * https://leetcode.com/problems/reverse-integer/description/
 *
 * algorithms
 * Easy (25.47%)
 * Likes:    2406
 * Dislikes: 3726
 * Total Accepted:    789.7K
 * Total Submissions: 3.1M
 * Testcase Example:  '123'
 *
 * Given a 32-bit signed integer, reverse digits of an integer.
 *
 * Example 1:
 *
 *
 * Input: 123
 * Output: 321
 *
 *
 * Example 2:
 *
 *
 * Input: -123
 * Output: -321
 *
 *
 * Example 3:
 *
 *
 * Input: 120
 * Output: 21
 *
 *
 * Note:
 * Assume we are dealing with an environment which could only store integers
 * within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose
 * of this problem, assume that your function returns 0 when the reversed
 * integer overflows.
 *
 */
/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
  const boundry = Math.pow(2, 31);
  if (x > boundry || x < boundry * -1) {
    return 0;
  }
  const flag = x >= 0;
  const a = Math.abs(x)
    .toString(10)
    .split("")
    .reverse()
    .join("");
  const nu = parseInt(a, 10);
  console.log(flag ? nu : nu * -1);
  return flag ? nu : nu * -1;
};

reverse(Math.pow(2, 31) - 1);
