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


////////////////////////////////////////////////////////
//INPUT EXAMPLE tournamentWinner([["HTML", "C#"],["C#", "Python"],["Python", "HTML"]], [0, 0, 1])
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

  //ADDITIONAL SOLUTION
  const HOME_TEAM_WON = 1;

function tournamentWinner(competitions, results) {
  let currentBestTeam = '';
  const scores = {[currentBestTeam]: 0};

  for (let i = 0; i < competitions.length; i++) {
    const result = results[i]
    const [homeTeam, awayTeam] = competitions[i]

    const winningTeam = result === HOME_TEAM_WON ? homeTeam : awayTeam;

    updateScores(winningTeam, 3, scores);

    if (scores[winningTeam] > scores[currentBestTeam]) {
      currentBestTeam = winningTeam;
    }
  }
  // Write your code here.
  return currentBestTeam;
}

function updateScores(team, points,scores) {
  if (!(team in scores)) scores[team] = 0;

  scores[team] += points;
}

////////////////////////////////////////////////////////
//Completed this one in 5 minutes GOOD JOB ME

function isValidSubsequence(array, sequence) {
    let count = 0;

    for (let i = 0; i < array.length; i++) {
      let ele = array[i];
      if (count === sequence.length) break;
      if (ele === sequence[count]) {
        count++
      }
    }
    console.log(count);
    if (count === sequence.length) {
      return true;
    }
    return false;
  }
