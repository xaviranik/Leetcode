// https://leetcode.com/problems/contains-duplicate/

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums) {
  const seen = [];

  for (let i = 0; i < nums.length; i++) {
    if (seen.includes(nums[i])) {
      return true;
    }
    seen.push(nums[i]);
  }

  return false;
};

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums) {
  return nums.length === new Set(nums).size ? false : true;
};
