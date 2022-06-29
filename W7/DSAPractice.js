//Find the smallest difference between two numbers in a set of two ARRAYS
function smallestDifference(arrayOne, arrayTwo) {

    let sDif = Math.abs(arrayOne[0] - arrayTwo[0]);
    let finalArr = [arrayOne[0],arrayTwo[0]]

    for (let i = 0; i < arrayOne.length; i++) {
      let num1 = arrayOne[i];
      console.log(num1, 'this is the first number at position', i)
      for (let j = 0; j < arrayTwo.length; j++) {
        let num2 = arrayTwo[j];
            console.log(num2, 'this is the second number at position', j)
        if (Math.abs(num1 - num2) < sDif) {
          sDif = Math.abs(num1 - num2)
          finalArr = [num1,num2]
        }
      }
    }
    return finalArr;
  }

  // My solution
  // Below is his solution

  function smallestDifferenc(arrayOne, arrayTwo) {
    arrayOne.sort((a,b) => a - b);
    arrayTwo.sort((a,b) => a - b);
    let idxOne = 0;
    let idxTwo = 0;
    let smallest = Infinity;
    let current = Infinity;
    let smallestPair = [];

    while (idxOne < arrayOne.length && idxTwo < arrayTwo.length) { //super smart way to setup a loop for both arrays
        let firstNum = arrayOne[idxOne];
        let secondNum = arrayTwo[idxTwo];
        if (firstNum < secondNum) {
            current = secondNum - firstNum;
            idxOne++;
        } else if (secondNum < firstNum) {
            current = firstNum - secondNum;
            idxTwo++;
        } else {
            return [firstNum, secondNum];
        }
        if (smallest > current) {
            smallest = current;
            smallestPair = [firstNum, secondNum];
        }
    }
    return smallestPair;

}
