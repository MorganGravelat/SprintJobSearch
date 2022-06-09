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
//My immediate solution for tournamentWinner
function tournamentWinner(competitions, results) {
    let winners = {}
    let score = 0;
    let winner = ''

    for (let i = 0; i < results.length; i++) {
      if (results[i] > 0) {
        if (winners[competitions[i][0]]) {
          winners[competitions[i][0]]++
          if (winners[competitions[i][0]] > score) {
            score = winners[competitions[i][0]]
            winner = competitions[i][0]
          }
        }
        else {
          winners[competitions[i][0]] = 1
          if (winners[competitions[i][0]] > score) {
            score = winners[competitions[i][0]]
            winner = competitions[i][0]
          }
        }
      } else {
        if (winners[competitions[i][1]]) {
          winners[competitions[i][1]]++
        } else {
                winners[competitions[i][1]] = 1
                if (winners[competitions[i][1]] > score) {
                score = winners[competitions[i][1]]
                winner = competitions[i][1]
                }
          }
      }
    }

    return winner;
  }
