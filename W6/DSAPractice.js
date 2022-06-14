function sortedSquaredArray(array) {
    for (let i = 0; i < array.length; i++) {
      console.log(array[i] * array[i])
      array[i] = array[i] * array[i]
    }
    return array.sort(function(a, b){return a - b});
  }
//Squaring all numbers in an array and sorting them.
