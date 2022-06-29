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
