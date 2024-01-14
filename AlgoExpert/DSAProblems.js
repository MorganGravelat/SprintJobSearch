function* factorial(n) {
    if (n<2) return 1;
    let val = 1;
    for (let i = 1; i <= n; i++) {
        val *= i;
        yield val;
    }
};
//Starting a new page as I go at all the problems again.

//Number of Ways to split a String
var numWays = function(s) {
    const MODULO = 10 ** 9 + 7;
    const size = s.length;
    let count = 0;

    for (const char of s) {
        if (char === '1') count += 1;
    }
    if (count % 3) return 0;
    if (!count) return (size - 1) * (size - 2) / 2 % MODULO;
    let left = right = current = 0;

    count /= 3;

    for (const char of s) {
        if (char === '1') current += 1;
        if (current === count) left += 1;
        if (current === count * 2) right += 1;
    }
    return left * right % MODULO;
};

//Magnetic balls leetcode
position.sort((a,b)=> a-b);
let start = 0;
let end = position[position.length-1];
let ans = -1;
let mid = start + Math.floor((end-start)/2)
while(start < end){
    if(is_possible(position, mid, m)){
        ans = mid;
        start = mid +1;
    } else {
        end = mid
    }
    mid = start + Math.floor((end-start)/2)
}
return ans
};

var is_possible = function(position, mid, m){
let counter = 1;
let last_pos = position[0]

for(let i=0; i<position.length; i++){
    if(position[i] - last_pos >= mid){
        counter++;
        if(counter == m){
            return true
        }
        last_pos = position[i]
    }
}
return false
}
