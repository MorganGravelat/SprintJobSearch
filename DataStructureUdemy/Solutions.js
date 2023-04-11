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
