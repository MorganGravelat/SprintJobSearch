/**
 * @param {string} s
 * @return {boolean}
 */
 var isValid = function(s) {
    if (s.length % 2 !== 0) {
        return false;
    }
    if (!s.length) {
        return true;
    }

    let queue = [];

    let objBrackets = {")":"(","}":"{","]":"["}

    for (let i = 0; i < s.length; i++) {
        let ele = s[i];
        let top_queue;
        if (objBrackets[ele]) {
            if (objBrackets[ele] === queue[queue.length-1]) {
                queue.pop();
            }
            else {
                return false;
            }
        }
        else {
            queue.push(ele);
        }

    }
    if (queue.length) {
        return false;
    }
    return true;

};
//Workingg on Valid Parentheses Leet Code Problem Above

//Leet Code Reverse List Solution
var reverseList = function(head) {
    let reversed = null; //no reversed
    let current = head; //setting head to current
    while (current?.val !== undefined) { //current.val = 1,2,3,4,5,null
        let nex = current?.next
        current.next = reversed
        reversed = current
        current = nex
    }

    return reversed
};

//Kth largest
// My solution
// class KthLargest:

//     def __init__(self, k: int, nums: List[int]):
//         self.k = k
//         self.nums = nums

//     def add(self, val: int) -> int:
//         self.nums.append(val)
//         self.nums.sort()
//         return self.nums[len(self.nums) - self.k]
