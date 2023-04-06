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
