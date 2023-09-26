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
