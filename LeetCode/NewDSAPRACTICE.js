function twoNumberSum(array, targetSum) {
    //Check for edge case of empty array
    //create return array to put the numbers that add up to targetSum into
    //Take the array of numbers
    //Create a for loop iterating through the array using i
    //Within that for loop iterate through every other number int he array beyond the one selected on the first loop and create another loop
    if (array.length<2) return [];

    let targetNumbers = [];

    for (let i = 0; i < array.length; i++) {
      let num1 = array[i];
      for (let j = i+1; j < array.length; j++) {
        let num2 = array[j];
        if (num1 + num2 == targetSum) targetNumbers.push(num1,num2);
      }
    }

    return targetNumbers;

  }
  ///Faster version b elow
  function twoNumberSum(array, targetSum) {
    const numObj = {}

    for (const num of array) {
      const potMatch = targetSum - num
      if (potMatch in numObj) return [num, potMatch];
      else numObj[num] = true;
    }
    return []
  }
//Valid subsequence good O(n) time and O(1) space
function isValidSubsequence(array, sequence) { //
    let seq_i = 0;
   for (let i = 0; i < array.length; i++) {
     if (sequence[seq_i] == array[i]) {
       if (seq_i === sequence.length-1) {
         return true;
       } else {
         seq_i++;
       }
     }
   }
  return false;
}
function sortedSquaredArray(array) {
    if (array.length < 1) return [];
    for (let i = 0; i < array.length; i++) {
      array[i] = array[i]*array[i];
    }
    return array.sort((a,b) => a-b);
  }

//Tournament winner
function tournamentWinner(competitions, results) {
    // Make an object for each winner going through in a loop and then just loop the object for the highest
    let winnerObj = {};
    let winner = "";
    let hiScore = 0;
    for (let i = 0; i < competitions.length; i++) {
      if (results[i] === 0) {
        let win = competitions[i][1]
        if (win in winnerObj) {
          winnerObj[win]++;
          if (winnerObj[win] > hiScore) {
            hiScore = winnerObj[win];
            winner = win;
          }
        }
        else {
          winnerObj[win] = 1;
          if (winnerObj[win] > hiScore) {
            hiScore = winnerObj[win];
            winner = win;
          }

        }
      }
      else {
        let win = competitions[i][0]
        if (win in winnerObj) {
          winnerObj[win]++;
          if (winnerObj[win] > hiScore) {
            hiScore = winnerObj[win];
            winner = win;
          }
        }
        else {
          winnerObj[win] = 1;
          if (winnerObj[win] > hiScore) {
            hiScore = winnerObj[win];
            winner = win;
          }
        }
      }
    }
    // for (ele in winnerObj) {
    //   let score =
    //   if (winnerObj[ele] > hiScore) hiSco
    // }
    return winner;
  }
//// Non-Constructible Change
function nonConstructibleChange(coins) { //This is O(nlogn) time and O(1) space
    coins.sort((a,b) => a-b);
    //console.log(coins);
    let currentChangeCreated = 0;
    for (const coin of coins) { // 1,1,2,3,5,7,22
      if (coin > currentChangeCreated + 1) return currentChangeCreated + 1;

      currentChangeCreated += coin;
    }

    return currentChangeCreated + 1;
  }
///Transpose Matrix
function transposeMatrix(matrix) {
    const transposedMatrix  = [];
    for (let col = 0; col < matrix[0].length; col++) {
      const newRow=[];
      for (let row = 0; row < matrix.length; row++) {
        newRow.push(matrix[row][col]);
      }
      transposedMatrix.push(newRow);
    }
    return transposedMatrix;
  }
//Majority Element in python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return nums[n//2]
//Convert to title in java
class Solution {
    public String convertToTitle(int columnNumber) {
        StringBuilder sb=new StringBuilder("");
        while(columnNumber!=0)
        {
            columnNumber-=1;
            int rem=columnNumber%26;
            sb.append((char)(rem+65));
            columnNumber/=26;
        }
        sb=sb.reverse();
        return sb.toString();

    }
}
//Implement Stack Using Queues in javascript
var MyStack = function() {
    this.stack = [];
};

MyStack.prototype.push = function(x) {
    this.stack.push(x);
};

MyStack.prototype.pop = function() {
    if (this.stack.length === 0) {
        return null; // Or throw an error, as popping from an empty stack is undefined behavior
    }
    return this.stack.pop();
};

MyStack.prototype.top = function() {
    if (this.stack.length === 0) {
        return null; // Or throw an error
    }
    return this.stack[this.stack.length - 1];
};

MyStack.prototype.empty = function() {
    return this.stack.length === 0;
};
// Number of 1 bits in java
public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        int ans=0;
        //TC => O(k), where k is total number of set bits. set bit is 1. unset bit is 0.
         while(n!=0){
             n = n & (n-1);
            ans++;
        }

        return ans;
    }
}

class Solution {
    public:
        bool winnerOfGame(string color) {
            int n = color.size();
            int cntA = 0;
            int cntB = 0;
            for(int i=1; i<n-1; i++) {
                if(color[i-1] == 'A' and color[i] == 'A' and color[i+1] == 'A') cntA++;
                else if(color[i-1] == 'B' and color[i] == 'B' and color[i+1] == 'B') cntB++;
            }
            return cntA > cntB;
        }
    };

    class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        C = [0, 0]
        for g, xs in groupby(colors):
            n = sum(1 for _ in xs)
            C[g == 'B'] += max(0, n-2)
        return C[0] > C[1]
// Combination Sum in java using backtracking
class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
      List<List<Integer>> list = new ArrayList<>();
      Arrays.sort(candidates);
      backtrack(list, new ArrayList<>(), candidates, target, 0);
      return list;
    }
    public void backtrack(List<List<Integer>> list, List<Integer> temp, int[] nums, int remain, int start) {
        if(remain < 0) return;
        else if (remain == 0) list.add(new ArrayList<>(temp));
        else {
            for(int i = start; i < nums.length; i ++) {
                temp.add(nums[i]);
                backtrack(list, temp, nums, remain - nums[i], i);
                temp.remove(temp.size() - 1);
            }
        }
    }
}
// Multiply Strings in javascript on leetcode
/**
 * @param {string} num1
 * @param {string} num2
 * @return {string}
 */
var multiply = function(num1, num2) {
    return String(BigInt(num1)*BigInt(num2));
};
//Path Sum 2</>
// Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

// A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

/**
 * @param {TreeNode} root
 * @param {number} sum
 * @return {number[][]}
 */
var pathSum = function(root, sum) {
    if (root === null) return [];
    const res = [];
    backtrack(root, sum, res, []);
    return res;
  };

  function backtrack(root, sum, res, tempList) {
    if (root === null) return;
    if (root.left === null && root.right === null && sum === root.val)
      return res.push([...tempList, root.val]);

    tempList.push(root.val);
    backtrack(root.left, sum - root.val, res, tempList);

    backtrack(root.right, sum - root.val, res, tempList);
    tempList.pop();
  }

  // Edit Distance
  /**
 * @param {string} word1
 * @param {string} word2
 * @return {number}
 */
var minDistance = function(word1, word2) {
    const m = word1.length;
      const n = word2.length;


      const dp = new Array(m + 1).fill(0).map(() => new Array(n + 1).fill(0));


      for (let i = 0; i <= m; i++) {
        dp[i][0] = i;
      }

      for (let j = 0; j <= n; j++) {
        dp[0][j] = j;
      }


      for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
          if (word1[i - 1] === word2[j - 1]) {

            dp[i][j] = dp[i - 1][j - 1];
          } else {

            dp[i][j] = Math.min(
              dp[i][j - 1] + 1,
              dp[i - 1][j] + 1,
              dp[i - 1][j - 1] + 1
            );
          }
        }
      }

      return dp[m][n];
    };


    //Median of two arrays
    /**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    let merged = [];
    let i = 0, j = 0;

    while (i < nums1.length && j < nums2.length) {
        if (nums1[i] < nums2[j]) {
            merged.push(nums1[i++]);
        } else {
            merged.push(nums2[j++]);
        }
    }

    while (i < nums1.length) merged.push(nums1[i++]);
    while (j < nums2.length) merged.push(nums2[j++]);

    let mid = Math.floor(merged.length / 2);
    if (merged.length % 2 === 0) {
        return (merged[mid-1] + merged[mid]) / 2;
    } else {
        return merged[mid];
    }
};

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function (l1, l2) {
    let dummyHead = new ListNode(0); // Dummy head to simplify the code
    let current = dummyHead;
    let carry = 0;

    while (l1 || l2) {
        let x = l1 ? l1.val : 0;
        let y = l2 ? l2.val : 0;
        let sum = carry + x + y;

        carry = Math.floor(sum / 10);
        current.next = new ListNode(sum % 10);
        current = current.next;

        if (l1) l1 = l1.next;
        if (l2) l2 = l2.next;
    }

    if (carry > 0) {
        current.next = new ListNode(carry);
    }

    return dummyHead.next;
};

/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
    let charMap = {};
    let maxLength = 0;
    let start = 0;

    for (let end = 0; end < s.length; end++) {
        const currentChar = s[end];

        if (charMap[currentChar] >= start) {
            start = charMap[currentChar] + 1;
        }
        charMap[currentChar] = end;

        maxLength = Math.max(maxLength, end - start + 1)
    }

    return maxLength;
};
