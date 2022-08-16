/*
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.



Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true


Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109



Objective:
    - given array of numbers
    - find the duplicate numbers if any in the array
    - return true if duplicates appear else false

Edge-Cases:
    - Array is length 0 return false
    - Array is length 1 return false
Strategy:
    - check base case
    - Initialize a Hash Table Memo var with value of {}
    - Add nums to Hash table until all nums have been sorted through
    - Return true if any nums already inside hash table
    - O(n) Time O(n) space
*/



function hasDuplicates(nums) {
    if (nums.length <= 1) return false

    let memo = new Set();

    for (let i = 0; i < nums.length - 1; i++) {
        let num = nums[i]

        if (memo.has(num)) {
            return true
        }
        else {
            memo.add(num)
        }
    }
    return false

}

console.log(hasDuplicates([1,1,1,3,3,4,3,2,4,2]))
