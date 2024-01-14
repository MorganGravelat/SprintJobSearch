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
