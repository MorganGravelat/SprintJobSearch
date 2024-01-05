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

//Q6
#include <iostream>
#include <vector>

int longestIncreasingSubsequence(const std::vector<int>& nums) {
    int n = nums.size();
    if (n == 0) return 0;

    std::vector<int> dp(n, 1);

    for (int i = 1; i < n; ++i) {
        for (int j = 0; j < i; ++j) {
            if (nums[i] > nums[j] && dp[i] < dp[j] + 1) {
                dp[i] = dp[j] + 1;
            }
        }
    }

    int max_len = 0;
    for (int i = 0; i < n; ++i) {
        if (dp[i] > max_len) {
            max_len = dp[i];
        }
    }

    return max_len;
}

int main() {
    std::vector<int> nums = {10, 22, 9, 33, 21, 50, 41, 60, 80};
    int result = longestIncreasingSubsequence(nums);
    std::cout << "Length of Longest Increasing Subsequence: " << result << std::endl;
    return 0;
}


//Q7
#include <iostream>
#include <unordered_map>

class TrieNode {
public:
    std::unordered_map<char, TrieNode*> children;
    bool isEndOfWord;

    TrieNode() {
        isEndOfWord = false;
    }
};

class Trie {
public:
    Trie();
    void insert(const std::string& word);
    bool search(const std::string& word);
    bool startsWith(const std::string& prefix);
    // Implement deletion and other methods as needed.
private:
    TrieNode* root;
};

int main() {
    Trie trie;
    trie.insert("apple");
    bool searchResult = trie.search("apple"); // Should return true
    bool startsWithResult = trie.startsWith("app"); // Should return true
    return 0;
}
//Sqrt(x)
class Solution {
public:
    int mySqrt(int x) {
        // For special cases when x is 0 or 1, return x.
        if (x == 0 || x == 1)
            return x;

        // Initialize the search range for the square root.
        int start = 1;
        int end = x;
        int mid = -1;

        // Perform binary search to find the square root of x.
        while (start <= end) {
            // Calculate the middle point using "start + (end - start) / 2" to avoid integer overflow.
            mid = start + (end - start) / 2;

            // Convert mid to long to handle large values without overflow.
            long long square = static_cast<long long>(mid) * mid;

            // If the square of the middle value is greater than x, move the "end" to the left (mid - 1).
            if (square > x)
                end = mid - 1;
            else if (square == x)
                // If the square of the middle value is equal to x, we found the square root.
                return mid;
            else
                // If the square of the middle value is less than x, move the "start" to the right (mid + 1).
                start = mid + 1;
        }

        // The loop ends when "start" becomes greater than "end", and "end" is the integer value of the square root.
        // However, since we might have been using integer division in the calculations,
        // we round down the value of "end" to the nearest integer to get the correct square root.
        return static_cast<int>(std::round(end));
    }
};
//Climbing Stairs
class Solution {
public:
    int climbStairs(int n, unordered_map<int, int>& memo) {
        if (n == 0 || n == 1) {
            return 1;
        }
        if (memo.find(n) == memo.end()) {
            memo[n] = climbStairs(n-1, memo) + climbStairs(n-2, memo);
        }
        return memo[n];
    }

    int climbStairs(int n) {
        unordered_map<int, int> memo;
        return climbStairs(n, memo);
    }
};

//Remove Duplicates from Sorted List

class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {

        if(head==NULL)return head;


        ListNode* node=head;
        while(node and node->next){

            if(node->next->val==node->val){
                node->next = node->next->next;
            }

            else{
                node=node->next;
            }
        }

        return head;
    }
};

//Maximum Depth of Binary Tree
int maxDepth(TreeNode* root) {
        if(!root) return 0;
        int maxLeft = maxDepth(root->left);
        int maxRight = maxDepth(root->right);
        return max(maxLeft, maxRight)+1;
    }
