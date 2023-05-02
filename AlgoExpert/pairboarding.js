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
