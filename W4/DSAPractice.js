//The palindrome check
function isPalindrome(string) {
    const revChar = [];
    for (let i = string.length - 1; i >= 0; i--) {
        revChar.push(string[i]);
    }
    return string === revChar.join('');
}

//Nth number of fib sequence
function getNthFib(n, memo = {1: 0, 2: 1}) {
    if (n in memo) {
        return memo[n];
    } else {
        memo[n] = getNthFib(n-1, memo) + getNthFib(n-2, memo);
        return memo[n];
    }
}
