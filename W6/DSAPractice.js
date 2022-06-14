function sortedSquaredArray(array) {
    for (let i = 0; i < array.length; i++) {
      console.log(array[i] * array[i])
      array[i] = array[i] * array[i]
    }
    return array.sort(function(a, b){return a - b});
  }
//Squaring all numbers in an array and sorting them.

//Best Is Prime Number Equation
function isPrime(num){
    if (num === 2) return true;
    if (num % 2 === 0) return false;
    if (num < 2) return false;

    for (let i = 3; i <= Math.floor(Math.sqrt(num)); i+=2) {
      if (num % i === 0) return false;
    }
    return true;
  }

  function sortedPrimes(input_array){
    var result = [];
    for (let i = 0; i < input_array.length; i++) {
      let num = input_array[i];
      if (isPrime(num)) result.push(num);
    }
    let typedArray = Float32Array.from(result);
    let sortedArray = [...typedArray.sort()];
    return sortedArray;
  }
