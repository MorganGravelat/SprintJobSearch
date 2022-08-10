//NODE DEPTH is the distance from the root node to the node we are currently at.
/*
    *       1
    *      / \
    *     2   3
    *    / \ / \
    *   4  5 6  7
    *  / \
    * 8  9
*/

function allKindsOfNodeDepths(root) {
    if (!root) return 0;
    let memo = {};
    return nodeDepths(root, memo);
}
