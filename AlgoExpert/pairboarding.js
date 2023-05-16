// Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

//     Each row must contain the digits 1-9 without repetition.
//     Each column must contain the digits 1-9 without repetition.
//     Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

// Note:

//     A Sudoku board (partially filled) could be valid but is not necessarily solvable.
//     Only the filled cells need to be validated according to the mentioned rules.


    Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

// Output: true

function validSudoku(board) {
    for (let i=0; i<9;i++){
        for (let j=0; j<9; j++) {
            if(board[i][j] !== ".") {
                let num = 0;
                for (let k = 0; k < 9; k++) {
                    if (board[i][k] === board[i][j]) num++;
                    if(num>=2) return false;
                }
                num = 0
                for (let k = 0; k < 9; k++) {
                    if (board[k][j] === board[i][j]) num++;
                    if(num>=2) return false;
                }
                num = 0
                for (let k=Math.floor(i/3)*3; k < Math.floor(i/3)*3+3;k++) {
                    for (let l=Math.floor(j/3)*3; l<Math.floor(j/3)*3+3; l++){
                        if(board[k][l] === board[i][j]) num++;
                        if(num>=2) return false;
                    }
                }
            }
        }
    }
    return true
}
console.log(validSudoku(
    [["8","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
))



You are given an array arr[] of size n. You have to convert the array into a non-decreasing array. You can only remove numbers from the ends of the array. Which of the sets of operations will result in arr being sorted?
arr[7] ={4,3,3,8,4,5,2}

Pick ONE option
Remove 4,3,3,8 from the beginning of the array.
Remove 8,4,5,2 from the end of the array.
Remove 4 from the beginning of the array and 4, 5, 2 from the end of the array.
None of the above
// 1. Remove 4,3,3,8 from the beginning of the array.
// 2. Remove 8,4,5,2 from the end of the array.
// 3. Remove 4 from the beginning of the array and 4, 5, 2 from the end of the array.
// 4. None of the above
// The answer would be 1. Remove 4,3,3,8 from the beginning of the array. The resulting array would be [4,5,2] which is sorted in non-decreasing order

// A circular linked list can be used to implement

// O(n)
function twoColorable(edges) {
    const black = new Set();
    const white = new Set();

    return edges.every((neighbors, parent) => {
        if (white.has(parent)) {
            for (let node of neighbors) {
                if (white.has(node)) return false;
                black.add(node);
            }
        } else {
            black.add(parent);
            for (let node of neighbors) {
                if (black.has(node)) return false;
                white.add(node);
            }
        }
        return true;
    })
} //This function has a time of O(n) and a space of O(n)

function twoColorable(edges) {
  const colors = edges.map(_ => null);
  colors[0] = true;
  const stack = [0];

  while (stack.length > 0) {
    const node = stack.pop();
    for (const connection of edges[node]) {
      if (colors[connection] === null) {
        colors[connection] = !colors[node];
        stack.push(connection);
      } else if (colors[connection] === colors[node]) {
        return false;
      }
    }
  }

  return true;
} //This function has a time of O(n) and a space of O(n)

//Rotate Array
function reverse(a, i, j){

    let li = i;

    let ri = j;

    while(li<ri){

        let temp = a[li];

        a[li++] = a[ri];

        a[ri--] = temp;
    }

}
var rotate = function(nums, k) {

 // to decrease computation for same result
  k = k % nums.length;

  // if k is negative
  // if(k < 0)

  // k = k + nums.length;


  //part 1
  //reverse left part
  reverse(nums, 0, nums.length-k-1);

  //part 2
  //reverse right part
   reverse(nums, nums.length-k, nums.length-1);

  //all

  reverse(nums, 0, nums.length-1);

  return nums;
};

//Interleaving String
var isInterleave = function(s1, s2, s3) {
    const dp = new Map();
    const solve = (a = 0, b = 0, c = 0) => {
        if(c == s3.length) return a == s1.length && b == s2.length;
        const key = [a, b, c].join(':');

        if(dp.has(key)) {
            // console.log('hit');
            return dp.get(key);
        }

        let takeS1 = false, takeS2 = false;
        if(s1[a] == s3[c]) takeS1 = solve(a + 1, b, c + 1);
        if(s2[b] == s3[c]) takeS2 = solve(a, b + 1, c + 1);

        dp.set(key, takeS1 || takeS2);
        return takeS1 || takeS2;
    }
    return solve();
};
