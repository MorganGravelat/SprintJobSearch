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
//NON CONTRUCTIBLE CHANGE PROBLEM
//If you do not know how to solve a problem, in array problems sort the input array and play around with the array
//You have an array like [5,7,1,1,2,3,22] and you want to find the smallest number that you cannot make
// YOu can sort the array into [1,1,2,3,5,7,22] and then you can see that the smallest number you cannot make is 20
// If the first value of the sorted list is not 1 then you can return 1
// YOu can go through and add the numbers 1 + 1 = 2, 2 + 2 = 4, 4 + 3 = 7, 7 + 5 = 12, 12 + 7 = 19, 19 + 22 = 41
// You can see that the smallest number you cannot make is 20 since all numbers added make 19
// We have a set of coins U = [1] all coins in the set
// We have a set of coins V = 1
// C = 1
// We can use math if V > C+1 then we can return C+1
// If V <= C+1 then we can add V to C and set V = C + V
// We can do this for all the coins in the array
//This would be O(n log n) time and O(1) space'
function nonConstructibleChange(coins) {
    let newCoins = coins.sort( function( a , b){
      if(a > b) return 1;
      if(a < b) return -1;
      return 0;
  });
    let currentChangeCreated = 0
    for (let i = 0; i < coins.length; i++) {
      coin = coins[i]
      if (coin > currentChangeCreated + 1) {
        return currentChangeCreated+1
      }
      currentChangeCreated += coin
    }
    return currentChangeCreated+1
  }
