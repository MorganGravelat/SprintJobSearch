/*
Right Sibling Tree Algo

*/

class BinaryTree {

    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

function rightSiblingTree(root) {
    MutationEvent(root, null, null);
    return root;
}

function mutate(node, parent, isLeftChild) {

    if (node === null) return;
    const (left, right) = node;
    mutate(left , node, true);
    if (parent === null) {
        node.right = null;
    } else if (isLeftChild) {
        node.right = parent.right;
    } else {
        if (parent.right === null) {
            node.right = null;
        } else {
            node.right = parent.right.left;
        }
    }
    mutate(right , node, false);
}


/*
Split Binary Tree

class BinaryTree {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

// O(n) time | O(h) space
// h = height of tree
function splitBinaryTree(root) {
    const desiredSubtreeSum = getTreeSum(root) / 2;
    const canBeSplit = trySubttrees(root, desiredSubtreeSum)[1];
    rturn canBeSplit ? desiredSubtreeSum : 0;
}

function trySubtrees(node, desiredSubtreeSum) {
    if (node === null) return [0, false];

    const [leftSum, canBeSplitLeft] = trySubtrees(node.left, desiredSubtreeSum);
    const [rightSum, canBeSplitRight] = trySubtrees(node.right, desiredSubtreeSum);

    const currentTreeSum = node.value + leftSum + rightSum;
    const canBeSplit = canBeSplitLeft || canBeSplitRight || currentTreeSum === desiredSubtreeSum;
    return [ currentTreeSum, canBeSplit ];
}

function getTreeSum(node) {
    if (node === null) return 0;
    return node.value + getTreeSum(node.left) + getTreeSum(node.right);
}

*/
class Solution:
    def setZeroes(self, matrix):
	    zero_r, zero_c = set(), set()
	    for i in range(len(matrix)):
		    for j in range(len(matrix[0])):
			    if matrix[i][j] == 0:
				    zero_r.add(i)
				    zero_c.add(j)
	    for i in zero_r:
		    matrix[i] = [0] * len(matrix[0])
	    for j in zero_c:
		    for i in range(len(matrix)):
			    matrix[i][j] = 0
/*
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.
 

Write a solution to find the second highest salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).

The result format is in the following example.
*/
select max(salary) as secondhighestsalary
from employee 
where salary <> (select max(salary) from employee )
