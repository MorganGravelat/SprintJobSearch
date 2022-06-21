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

  function getPrimeFactors(num) {
    let returnArr = new Set();

    for (let i = 2; i <= num/2; i++) {
      if (num % i === 0 && isPrime(i)) {
        returnArr.add(i);
        returnArr.add(num/i);
      }

    }
    console.log(returnArr)
    return returnArr;

  }
  function primeFactors(input_array){
    var result = [];
    for (let i = 0; i < input_array.length; i++) {
      let primeFactors = getPrimeFactors(input_array[i]);
      if (primeFactors.length) result.push(primeFactors);
    }
    //for ( let i = 2; i < )
    return result; // array of arrays
    //if a prime factor goes into a number more than once, it is only included once
    // [6, 8, 9] -> [[2, 3], [2], [3]]
  }

  var input = [6];
  var result = sortedPrimes([3,5,6,7,11,17,19]);
  console.log(result);

  var result = primeFactors(input);
  console.log(result);




  /* Full Prime Group */
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

  function getPrimeFactors(num) {
    let factors = new Set([num]);
    for (let i = 2; i <= num/2; i++) {

      if (num % i === 0) {
        factors.add(i);
        factors.add(num/i);
      }

    }
    let returnArr = sortedPrimes([...factors])
    return returnArr;

  }
  function primeFactors(input_array){
    var result = [];
    for (let i = 0; i < input_array.length; i++) {
      let primeNumFactors = getPrimeFactors(input_array[i]);
      if (primeNumFactors.length) result.push([...primeNumFactors]);
    }
    //for ( let i = 2; i < )
    return result; // array of arrays
    //if a prime factor goes into a number more than once, it is only included once
    // [6, 8, 9] -> [[2, 3], [2], [3]]
  }

  var input = [97,10898,9];
  var result = sortedPrimes([3,5,6,7,11,17,19]);
  console.log(result);

  var result = primeFactors(input);
  console.log(result);
  let myNum = 10898


  class Solution:
    def convert(self, s: str, n: int) -> str:
        wordList = ['' for i in range(n)]

        curr = 0
        up = True
        for i in s:
            wordList[curr] += i

            if up:
                if curr + 1 < n:
                    curr += 1
                else:
                    curr -= 1
                    up = False
            else:
                if curr - 1 >= 0:
                    curr -= 1
                else:
                    curr += 1
                    up = True

        return ''.join(wordList)
