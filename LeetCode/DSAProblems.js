function* factorial(n) {
    if (n<2) return 1;
    let val = 1;
    for (let i = 1; i <= n; i++) {
        val *= i;
        yield val;
    }
};
//Starting a new page as I go at all the problems again.

//Number of Ways to split a String
var numWays = function(s) {
    const MODULO = 10 ** 9 + 7;
    const size = s.length;
    let count = 0;

    for (const char of s) {
        if (char === '1') count += 1;
    }
    if (count % 3) return 0;
    if (!count) return (size - 1) * (size - 2) / 2 % MODULO;
    let left = right = current = 0;

    count /= 3;

    for (const char of s) {
        if (char === '1') current += 1;
        if (current === count) left += 1;
        if (current === count * 2) right += 1;
    }
    return left * right % MODULO;
};

//Magnetic balls leetcode
position.sort((a,b)=> a-b);
let start = 0;
let end = position[position.length-1];
let ans = -1;
let mid = start + Math.floor((end-start)/2)
while(start < end){
    if(is_possible(position, mid, m)){
        ans = mid;
        start = mid +1;
    } else {
        end = mid
    }
    mid = start + Math.floor((end-start)/2)
}
return ans
};

var is_possible = function(position, mid, m){
let counter = 1;
let last_pos = position[0]

for(let i=0; i<position.length; i++){
    if(position[i] - last_pos >= mid){
        counter++;
        if(counter == m){
            return true
        }
        last_pos = position[i]
    }
}
return false
}

//1554. Strings Differ by One Character
var differByOne = function(dict) {
    if(!dict.length) return false;
    // Here we calculate the expected runtime of the two alternative
    // solutions to see which strategy to apply
	let sol1 = Math.pow(dict[0].length, 2) * dict.length;
    let sol2  = dict.length * dict.length;
	// We are switching strategies depending on which has better efficiency
	// Thanks @ThabetS for suggesting a replacement for hardcoded dict[0].length
    if(sol1 < sol2) {
        // This algorithm is fast with words that are short however it falls apart
        // as word length increases and eventually fails due to memory limits
        const found = new Set();
        for(let word of dict) {
            for(let i = 0; i < word.length; i++) {
                const key = word.slice(0,i) + '*' + word.slice(i+1, word.length);
                if(found.has(key)) return true;
                found.add(key);
            }
        }
        return false;
    } else {
        // This algorithm is better against small N of words. Since this problem
        // is constrained by the *total number of characters in the question*
        // we know that dictionaries containing long words must have small N
        for(let i = 0; i < dict.length; i++) {
            for(let j = i+1; j < dict.length; j++) {
                if(compareTwoStrings(dict[i], dict[j])) return true;
            }
        }
        return false;
    }
};

function compareTwoStrings(string1, string2) {
    let misses = 0;
    for(let i = 0; i < string1.length; i++) {
        if(string1[i] !== string2[i]) {
            misses++;
            if(misses > 1) return false;
        }
    }
    return true;
}

//1577. Number of Ways Where Square of Number Is Equal to Product of Two Numbers
//Smart way using hashmaps by anna-hcj user
var numTriplets = function(nums1, nums2) {
    return getTriplets(nums1, nums2) + getTriplets(nums2, nums1);

    function getTriplets(nums1, nums2) {
      let ans = 0;
      for (let i = 0; i < nums1.length; i++) {
        let target = nums1[i] * nums1[i], map = new Map();
        for (let j = 0; j < nums2.length; j++) {
          ans += map.get(target / nums2[j]) || 0;
          map.set(nums2[j], (map.get(nums2[j]) || 0) + 1);
        }
      }
      return ans;
    }

//More along of what I tried to do when attempting this
var numTriplets = function(nums1, nums2) {
    nums1.sort((a, b) => a - b);
    nums2.sort((a, b) => a - b);
    return calc(nums1, nums2) + calc(nums2, nums1);

    function calc(nums1, nums2) {
      let ans = 0;
      for (let i = 0; i < nums1.length; i++) {
        let target = nums1[i] * nums1[i];
        let j = 0, k = nums2.length - 1;
        while (j < k) {
          if (nums2[j] * nums2[k] === target) {
            if (nums2[j] === nums2[k]) { // case 2: [nums2[j], ..., nums2[k]] are all equal
              ans += (k - j) * (k - j + 1) / 2;
              j = k;
            } else { // case 1: nums2[j] !== nums2[k]
              let left = j, right = k;
              while (j < k && nums2[j] === nums2[left]) j++;
              while (k >= 0 && nums2[k] === nums2[right]) k--;
              ans += (j - left) * (right - k);
            }
          }
          else if (nums2[j] * nums2[k] < target) j++;
          else k--;
        }
      }
      return ans;
    }
  };

  int removeElement(vector<int>& nums, int val) {
    while(true)
    {
        auto it = find(nums.begin(),nums.end(),val);

        if(it != nums.end())
            nums.erase(it);
        else break;
    }
    return nums.size();
}

var removeDuplicates = function(nums) {
    let count = 1; // Initialize the count of unique elements to 1
  for (let i = 1; i < nums.length; i++) {
    if (nums[i] !== nums[count - 1]) {
      nums[count] = nums[i];
      count++;
    }
  }
  return count;
};

var strStr = function (haystack, needle) {
    function findFrom(i) {
      if (haystack[i] === undefined) return -1;
      if (haystack[i] === needle[0]) {
        const initial = i;
        i++;
        let next = -1; // In case the first letter appears again
        let j = 1;
        let matches = true;
        while (needle[j]) {
          if (haystack[i] === needle[0] && next === -1) next = i;
          if (needle[j] !== haystack[i]) {
            if (next !== -1) return findFrom(next);
            matches = false;
            break;
          }
          i++;
          j++;
        }

        if (matches) return initial;
        return findFrom(i);
      }
      return findFrom(++i);
    }

    return findFrom(0);
  };
//4sum
  /**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[][]}
 */
var fourSum = function(nums, target) {
    let res=[]
    nums.sort((a,b)=>a-b)
    for(let i=0;i<nums.length;i++){
        if(i>0 && nums[i] == nums[i-1]){
            continue;
        }
        let left1 = i+1;

        // while(left1<nums.length-1){
        for(var j=left1;j<nums.length;j++){
            if(j>left1 && nums[j] == nums[j-1]){
              continue;
            }
            let left = j+1;
            let right = nums.length-1;
          while(left<right){
            let sum = nums[i]+nums[j]+nums[left]+nums[right]
            if(sum>target){
                right--;

            }else if(sum<target){
                left++
            }else{
                res.push([nums[i],nums[j],nums[left],nums[right]])
                left++;
                while(nums[left] == nums[left-1]){
                    left++
                }
            }
          }

        }

    }
    return res
};

//Next permutation
/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var nextPermutation = function(nums) {
    const n = nums.length;
    // Step 1. scan from right and find the first digit that is less than its right
    for (let i = n - 2; i >= 0; i--) {
        if (nums[i] < nums[i + 1]) {
        // Step 2. scan from right and find the digit that is larger than nums[i]
        for (let j = n - 1; j > i; j--) {
            if (nums[j] > nums[i]) {
            // Step 3. swap nums[i] and nums[j], reverse from i+1
            swap(nums, i, j);
            reverse(nums, i + 1, n - 1);
            return;
            }
        }
        }
    }
    nums.reverse();
};


const swap = (nums, i, j) => ([nums[i], nums[j]] = [nums[j], nums[i]]);

const reverse = (nums, start, end) => {
  while (start < end) {
    swap(nums, start++, end--);
  }
};


/**
 * @param {number[]} candyType
 * @return {number}
 */
var distributeCandies = function(candyType) {
    let set = new Set(candyType);
    let n = candyType.length/2;
    let ret = 0;
    if (set.size>=n) {
        ret = n;
    } else {
        ret = set.size;
    }
    return ret;

};

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
/*
Objective:
-Given an array of integers nums sorted in non-descreasing order and a target value
-Find the starting and ending positions of the target value in the array
-Return [-1,-1] if the target is not found
-Implement the algorithm with O(log n) runtime complexity

Edge Cases:
-If the input array is emptyj(nums.length is 0) Return [-1,-1]

-Initialize array 'arr' with [-1,-1] to store the starting and ending  positions of the target.
-Initialize variables 'l' and 'r' representing the left and right
-If 'nums[mid]' is equal to the target I am looking for
-Update 'arr[0]' with middle staarting position
-Update 'r' to middle-1 to search in the left half
-If nums at middle is less than the target, update 'l' to middle positon + 1
-If nums at middle is greater than the target, update 'r' to middle position - 1

*/
var searchRange = function(nums, target) {
    let arr = [-1, -1]; // [3,4]

    let l = 0; // 3
    let r = nums.length - 1; //2

    while (l<=r) {
        let mid = Math.floor((l+r)/2); //2/4/3
        if (nums[mid] === target) { //nums //7 === 8/8/8
            arr[0] = mid; //4
            r = mid-1;
        } else if (nums[mid] < target) { //
            l = mid + 1 //l3
        } else {
            r = mid - 1;
        }
    }

    l = 0; //5
    r = nums.length - 1; //4

    while (l<=r) { //
        let mid = Math.floor((l+r)/2); //5
        if (nums[mid] === target) {
            arr[1] = mid;
            l = mid + 1;
        } else if (nums[mid] < target) {
            l = mid+1;
        } else {
            r = mid - 1;
        }
    }
    return arr;
};
///ROTATED SORTED ARRAY BELOW
class Solution {
    int search(int[] nums, int target) {
       int pivot=findPivot(nums);
       if(pivot==-1){
          return binarySearch(nums,target,0,nums.length-1);
       }
       if(nums[pivot]==target){
           return pivot;
       }
       if(nums[0]>target){
          return binarySearch(nums,target,pivot+1,nums.length-1);
       }
      return binarySearch(nums,target,0,pivot-1);

   }
  int findPivot(int []arr){
       int start=0;
       int end=arr.length-1;
       while(start<=end){
       int mid=start+(end-start)/2;
       if( mid<end && arr[mid]>arr[mid+1]){
           return mid;
       }
       if(  mid>start && arr[mid-1]>arr[mid]){
           return mid-1;
       }
       if(arr[start]>=arr[mid]){
           end=mid-1;
       }
       if(arr[start]<arr[mid]){
           start=mid+1;
       }

      }
        return -1;
}
   int binarySearch(int []arr,int target,int s,int e){
          while(s<=e){
           int mid=s+(e-s)/2;
           if(arr[mid]==target){
               return mid;
           }
           if(arr[mid]>target){
               e=mid-1;
           }
           else{
               s=mid+1;
           }

          }
            return -1;
   }
}

//Hard Regular Expression Matching Problem
var isMatch = function(s, p) {
    const m = s.length, n = p.length;
    const dp = new Array(m+1).fill().map(() => new Array(n+1).fill(false));
    dp[0][0] = true; // empty pattern matches empty string

    // initialize first row (empty string)
    for (let j = 1; j <= n; j++) {
        if (p[j-1] === '*')
        dp[0][j] = dp[0][j-2];
    }

    // fill in remaining cells
    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
        if (s[i-1] === p[j-1] || p[j-1] === '.') {
            dp[i][j] = dp[i-1][j-1];
        } else if (p[j-1] === '*') {
            dp[i][j] = dp[i][j-2]; // zero occurrences
            if (s[i-1] === p[j-2] || p[j-2] === '.') {
            dp[i][j] = dp[i][j] || dp[i-1][j]; // one or more occurrences
            }
        }
        }
    }
    return dp[m][n];
}

/**
 * @param {string} s
 * @param {string[]} words
 * @return {number[]}
 */
var findSubstring = function (s, words) {
    let wordLen = words[0].length
    let totalWords = words.length
    let subStrLen = wordLen * totalWords

    let cache = {}
    function checkString(str) {
        if (str in cache) {
            return cache[str]
        }
        let tempWords = [...words]
        for (let i = 0; i < totalWords; i++) {
            let w = str.slice(i * wordLen, (i + 1) * wordLen)
            let index = tempWords.indexOf(w)
            if (index >= 0) {
                tempWords[index] = null
            } else {
                cache[str] = false
                return cache[str]
            }
        }
        cache[str] = true
        return cache[str]
    }

    let result = []
    let maxIndex = (s.length - subStrLen)
    for (let i = 0; i <= maxIndex; i++) {
        let subStr = s.slice(i, subStrLen + i)
        if (checkString(subStr)) {
            result.push(i)
        }
    }
    return result
};

/**
 * @param {number[]} height
 * @return {number}
 */
const trap = function(height) {
    let left = 0;
    let right = height.length - 1;
    let maxHeightLeft = height[left];
    let maxHeightRight = height[right];
    let water = 0;
    while (left < right) {
        if (maxHeightLeft < maxHeightRight) {
            left++;
            if (height[left] < maxHeightLeft) {
                water += maxHeightLeft - height[left];
            } else {
                maxHeightLeft = height[left];
            }
        } else {
            right--;
            if (height[right] < maxHeightRight) {
                water += maxHeightRight - height[right];
            } else {
                maxHeightRight = height[right];
            }
        }
    }
    return water;
};

/**
 * @param {string} s
 * @param {string} p
 * @return {boolean}
 */
var isMatch = function(s, p) {
    let dp = [];
    var recur = function(s, p) {
        if (!dp[s]) dp[s] = {};
        if (dp[s][p] != null) return dp[s][p];

        if (s == p || (p.includes('*') && !p.replace(/\*/g, ''))) {
            dp[s][p] = true;
        } else if (s.length == 0 || p.length == 0) {
            dp[s][p] = false;
        } else if (p[0] == '?' || p[0] == s[0]) {
            dp[s][p] = recur(s.slice(1), p.slice(1));
        } else if (p[0] == '*') {
            dp[s][p] = recur(s.slice(1), p) || recur(s, p.slice(1));
        } else {
            dp[s][p] = false;
        }
        return dp[s][p];
    }
    return recur(s, p);
};

var firstMissingPositive = function(nums) {
    nums.sort((a,b) => a-b)
    let index = nums.indexOf(1);

    if(index === -1)return 1
    // console.log(index)

    for(index+1; index < nums.length; index++) {
      if(nums[index+1] !== nums[index] +1 && nums[index+1] !== nums[index]){
            return nums[index]+1
        }
    }

    return nums[index]+1
};
