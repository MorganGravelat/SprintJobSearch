function sortedSquaredArray(array) {
    for (let i = 0; i < array.length; i++) {
      console.log(array[i] * array[i])
      array[i] = array[i] * array[i]
    }
    return array.sort(function(a, b){return a - b});
  }
//Squaring all numbers in an array and sorting them.


function isPrime(num){
    if (num === 2) return true;

    if (num % 2 === 0) return false;

    if (num < 2) return false;

    for (let i = 3; i <= math.floor(math.sqrt(num)); i+=2) {
      if (num % i === 0) return false;
    }
    return true;
}
