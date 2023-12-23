//Q1
#include <iostream>
#include <vector>

int maxSubarraySum(const std::vector<int>& arr) {
    int n = arr.size();
    if (n == 0) return 0;

    int incl = arr[0];
    int excl = 0;

    for (int i = 1; i < n; ++i) {
        int new_excl = (incl > excl) ? incl : excl;
        incl = excl + arr[i];
        excl = new_excl;
    }

    return (incl > excl) ? incl : excl;
}

int main() {
    std::vector<int> arr = {1, 2, 3, 4, 5};
    int result = maxSubarraySum(arr);
    std::cout << "Maximum Subarray Sum: " << result << std::endl;
    return 0;
}

//Q2
#include <iostream>
#include <string>
#include <vector>

struct PalindromicNode {
    std::vector<int> next;
    int length;
    int suffixLink;
};

class PalindromicTree {
public:
    PalindromicTree(const std::string& str);
    // Implement methods to build and query the tree.
private:
    std::string s;
    std::vector<PalindromicNode> tree;
};

int main() {
    std::string str = "abacaba";
    PalindromicTree tree(str);
    // Use tree to query palindromes.
    return 0;
}

//Q3
#include <iostream>
#include <vector>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

int diameter = 0;

int calculateHeight(TreeNode* root) {
    if (root == nullptr) return 0;

    int leftHeight = calculateHeight(root->left);
    int rightHeight = calculateHeight(root->right);

    diameter = max(diameter, leftHeight + rightHeight);

    return 1 + max(leftHeight, rightHeight);
}

int treeDiameter(TreeNode* root) {
    if (root == nullptr) return 0;
    calculateHeight(root);
    return diameter;
}

int main() {
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);

    int result = treeDiameter(root);
    cout << "Diameter of the tree is: " << result << endl;

    return 0;
}

//Q4
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

bool isConnected(vector<vector<int>>& graph, int start, int end) {
    int n = graph.size();
    vector<bool> visited(n, false);
    queue<int> q;
    q.push(start);

    while (!q.empty()) {
        int current = q.front();
        q.pop();
        visited[current] = true;
        if (current == end) return true;

        for (int neighbor : graph[current]) {
            if (!visited[neighbor]) {
                q.push(neighbor);
            }
        }
    }

    return false;
}

int main() {
    int n = 6; // Number of nodes
    vector<vector<int>> graph(n);
    graph[0] = {1, 2};
    graph[1] = {0, 2};
    graph[2] = {0, 1};
    graph[3] = {4, 5};
    graph[4] = {3, 5};
    graph[5] = {3, 4};

    int start = 0, end = 3; // Nodes to check for connectivity
    bool connected = isConnected(graph, start, end);

    if (connected) {
        cout << "Nodes " << start << " and " << end << " are connected." << endl;
    } else {
        cout << "Nodes " << start << " and " << end << " are not connected." << endl;
    }

    return 0;
}

//Q5
#include <iostream>
#include <stack>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

int kthSmallest(TreeNode* root, int k) {
    stack<TreeNode*> s;
    TreeNode* current = root;

    while (current || !s.empty()) {
        while (current) {
            s.push(current);
            current = current->left;
        }

        current = s.top();
        s.pop();
        k--;
        if (k == 0) return current->val;

        current = current->right;
    }

    return -1; // If k is out of bounds
}

int main() {
    TreeNode* root = new TreeNode(3);
    root->left = new TreeNode(1);
    root->right = new TreeNode(4);
    root->left->right = new TreeNode(2);

    int k = 1;
    int result = kthSmallest(root, k);
    cout << "The " << k << "th smallest element is: " << result << endl;

    return 0;
}
