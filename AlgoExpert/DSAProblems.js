function threeNumberSum(arr, targetSum) {
    arr.sort((a,b) => a - b);
    const threes = [];
    for (let i = 0; i < arr.length - 2; i++) {
      let left = i + 1;
      let right = arr.length - 1;
      while (left < right) {
        const currentSum = arr[i] + arr[left] + arr[right];
        if (currentSum === targetSum ) {
          threes.push([arr[i], arr[left], arr[right]]);
          left++;
          right--;
        } else if (currentSum < targetSum) {
          left++;
        } else if (currentSum > targetSum) {
          right--;
        }
      }
    }
    return threes
}
//firstDuplicateValue problem Algo Expert
function firstDuplicateValue(array) {
    numbers_found = {} // I used a hash table to store the numbers I've seen
    for (let i = 0; i < array.length; i++) {
      ele = array[i] //
      if (!(ele in numbers_found)) {
        numbers_found[ele] = ele
      }
      else {
        return ele
      }
    }
    return -1;
  }
