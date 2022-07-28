function noDupe(array) { //[2, 3, 2]
    if (array.length === 0) return 0;
    let i = 0;
    let memo = {}
    for (let j = 1; j < array.length; j++) {
        if (!(array[j] in memo)) {
            i++; // 1
            memo[array[j]] = 0
        }
    }

    return i+1;
}

console.log(noDupe([1,2,3,5,8,2,2,29,4,2,2]))
//                    1 2 3 4 4 4 5
