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

//Isomorphic Strings
class Solution {
public:
    bool isIsomorphic(string s, string t) {
         unordered_map<char, char> mp, mp2;
        for (int i=0; i<s.length(); ++i) {
            if (mp[s[i]] && mp[s[i]]!=t[i]) return false;
            if (mp2[t[i]] && mp2[t[i]]!=s[i]) return false;
            mp[s[i]]=t[i];
            mp2[t[i]]=s[i];
        }
        return true;
    }
};

// Reverse Linked List
class Solution {
public:
    ListNode* reverseList(ListNode* head) {

        ListNode* prev = NULL;
        ListNode* curr = head;

        while(curr != NULL){
            ListNode* forward = curr->next;
            curr->next = prev;
            prev = curr;
            curr = forward;

        }
        return prev;
    }
};

//Invert Binary Tree
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    void solve(TreeNode* root){
        if(root == NULL){
            return;
        }
        TreeNode* le = root->left;
        root->left = root->right;
        root->right = le;
        solve(root->left);
        solve(root->right);
    }

    TreeNode* invertTree(TreeNode* root) {
        TreeNode* ans = root;
        solve(root);
        return ans;
    }
};

/**
 * @param {number[]} nums
 * @return {number[][]}
 */

var threeSum = function(nums) {
    nums.sort((a,b) => a-b);
    const result = [];

    for (let i = 0; i < nums.length - 2; i++) {

        if (i > 0 && nums[i] === nums[i - 1]) {
            continue;
        }

        let left = i + 1;
        let right = nums.length - 1;

        while (left < right) {
            const sum = nums[i] + nums[left] + nums[right];

            if (sum === 0) {
                result.push([nums[i], nums[left], nums[right]]);

                while (left < right && nums[left] === nums[left + 1]) {
                    left++;
                }
                while (left < right && nums[right] === nums[right + 1]) {
                    right--;
                }
                left++;
                right--;
            } else if (sum < 0) {
                left++;
            } else {
                right--;
            }
        }
    }
    return result;
};

const nums = [81,-106,126,107,-1,97,-188,169,4,-162,-147,170,-199,-120,149,96,-97,-140,85,156,-120,34,-20,-46,-63,66,97,-56,-32,-17,36,-28,12,20,-46,86,52,-51,-113,-194,124,-104,-22,47,21,178,121,102,186,123,120,70,-61,4,198,-90,-189,-198,3,-141,96,165,198,32,-195,-17,81,-106,-113,146,83,108,45,160,30,102,48,46,6,102,-61,-196,186,-113,-174,-51,-143,191,148,-61,181,-65,50,-104,-30,-196,-157,-195,-103,167,95,-153,-181,-101,-96,-55,130,109,-102,42,-5,-112,-76,-184,-156,137,194,6,-157,123,77,-176,-2,16,-19,-170,99,101,40,-10,-28,-8,16,-43,1,-43,-158,-93,24,16,132,-154,36,-73,20,-96,-181,108,-101,55,187,61,-101,-80,-80,191,-89,-162,139,48,-147,194,-12,-58,92,-169,105,26,-140,-46,7,-195,22,159,-82,22,0,-186,7,-63,52,63,135,-171,-80,-168,-150,44,-169,-51,-70,-33,-149,183,11,33,105,-90,158,-132,-158,74,-105,-135,-111,150,-138,37,78,131,98,35,121,-131,49,-129,151,23,56,188,-34,-200,-54,-111,180,185,127,-31,-92,-15,107,60,163,-68,162,-6,183,92,164,8,-199,103,60,-158,69,-29,144,-167,187,71,27,90,54,-53,-175,-64,-109,71,-105,-200,167,44,-154,-55,158,-89,97,-114,70,-127,-185,48,16,129,-64,103,116,28,-70,-176,26,-190,151,-1,1,-38,7,182,-186,186,-85,136,42,-159,-31,9,99,-133,199,15,137,-190,-26,-101,-3,104,-31,35,-188,176,-189,-158,-85,39,-6,53,-57,-82,161,-142,-65,-65,108,-61,-29,-185,50,69,93,185,68,-116,-187,-11,-188,124,40,-70,138,-125,-143,33,74,85,39,-15,-83,-170,147,158,28,-147,-4,3,-50,-35,133,20,182,186,39,137,167,74,-169,-111,-135,-151,81,125,113,-153,18,-134,-101,-77,-178,-141,87,113,-120,-26,-86,35,187,80,150,-198,149,-35,-144,193,-174,165,167,-159,-197,-114,-185,-180,-191,-45,-54,114,36,-148,-197,128,-129,-152,136,87,86,-96,160,41,-134,-85,18,181,172,-79,185,-79,-103,139,-159,-61,45,40,-1,22,40,27,-93,-51,73,-78,68,10,-54,-128,-31,-38,11,-11,-175,-162,197,-36,-32,152,67,23,-92,-84,124,-30,-154,-48,37,170,-33,-53,-17,-29,161,-13,-132,-36,-121,-120,-87,118,-24,142,127,-35,109,-160,-8,-91,36,90,54,196,77,169,114,19,21,51,-52,-63,-131,110,-144,68,-167,-186,-136,138,77,77,26,37,111,165,35,-117,-122,-24,-146,146,-173,0,-45,-19,9,125,-89,159,-187,-2,78,150,133,-196,-82,48,92,-36,22,85,-187,95,155,-119,20,63,-163,140,-129,127,75,-159,94,-136,-12,-142,-78,-186,15,-170,180,-135,-31,86,-180,83,-124,115,13,22,182,97,145,-104,146,-38,10,155,-138,166,-173,-179,67,-60,156,-108,139,-199,-170,-149,11,-75,150,-170,95,39,153,33,71,-132,-98,52,187,87,6,7,155,131,-25,-153,-133,-127,4,-106,-172,176,33,197,130,84,-82,-189,16,62,73,-104,133,-100,94,-167,38,-28,166,-37,-73,-179,-187,3,194,99,-83,153,7,-156,6,-91,41,15,66,-197,153,166,72,32,107,93,124,-193,-64,1,-145,7,152,-83,15,-89,29,-30,-125,-166,-199,187,-177,148,164,165,-156,-17,-40,106,-6,89,-122,-18,-31,-65,138,21,-112,113,123,-45,81,102,81,-43,75,-1,88,-199,129,-47,19,57,-169,-30,177,23,85,-27,129,175,94,-31,-12,-92,-11,32,-114,-68,-109,183,-118,163,-31,-109,-21,-96,17,193,72,-101,-68,12,-142,-108,-133,5,183,97,-1,-85,-69,9,163,40,182,5,-140,60,167,-155,-157,186,-58,-173,182,-64,-83,61,144,56,-33,-32,103,22,-164,-57,-152,98,-7,165,45,-113,163,153,-66,-40,-109,83,-9,109,26,54,58,-77,-25,-53,50,157,-61,-167,-3,-144,165,-3,37,-124,28,72,-27,49,9,-148,185,-138,29,-13,-156,139,-31,193,-151,-135,-55,193,86,-19,-80,-23,-185,135,153,-36,-182,-145,160,-167,-155,141,-85,51,-200,-126,-173,-108,-162,-39,198,26,161,116,177,45,-13,-52,48,-200,104,-40,121,-158,-148,-36,133,-57,60,121,155,43,-122,-94,73,-47,41,142,191,93,-90,145,110,-37,-142,64,-168,135,62,105,-142,8,35,138,13,112,-81,192,1,-134,-17,-17,-185,95,33,57,-7,27,31,154,0,79,-176,-68,-56,-184,71,46,-143,-122,-65,36,-68,169,-5,12,192,58,-1,-184,-181,-151,-142,-58,117,117,-120,121,-19,-178,-110,-131,121,74,72,41,13,140,-58,70,169,49,35,-132,89,57,173,3,79,184,181,-103,-125,51,177,-107,68,-185,-188,111,86,-81,187,4,-49,131,156,42,172,106,-79,158,-107,-12,-178,88,-142,73,-152,15,194,173,-142,-180,80,-143,86,50,162,65,190,57,76,145,124,65,26,30,-6,94,154,116,126,-19,-118,-131,106,23,60,-78,12,192,-112,123,168,-20,80,156,-78,59,127,77,-176,-121,-32,-52,181,40,44,-183,89,83,-172,193,195,-151,93,-19,-145,158,115,-49,131,186,55,-178,-60,5,183,-155,35,-15,-2,-71,-181,66,-81,-18,48,-174,-48,-194,33,56,-21,-114,-155,-63,-73,-65,20,-106,-187,77,142,189,-103,164,-173,-41,-149,66,156,42,-7,197,105,80,-124,-138,-145,-33,-96,-32,-17,-169,-5,27,-19,165,-63,-188,-88,70,-108,67,-59,77,-86,-96,-139,189,-7,60,-126,-16,46,-141,181,109,-11,-9,40,-194,-38,169,-47,-31,-158,-178,-138,22,34,1,-125,113,21,-160,199,31,-63,23,-184,-109,-197,14,-50,139,-97,-132,154,-121,-151,55,150,-57,26,70,-147,121,91,69,0,142,184,126,-5,187,93,46,109,107,137,175,189,-19,49,-50,122,-181,169,-193,-65,161,-84,-89,87,-140,-20,126,-49,23,-118,-150,17,75,135,167,-62,51,124,136,-124,-197,-79,173,-134,166,-190,-23,-76,-16,-9,180,-100,171,-137,79,167,-37,-145,125,5,170,24,156,9,-57,141,-162,10,66,178,-89,-118,-138,-158,-151,-64,148,87,-94,-155,-47,51,-200,-43,164,-188,148,-142,63,102,143,179,50,72,47,-107,161,-162,26,-31,-118,-183,13,5,21,-190,135,14,-197,-181,-49,130,56,-72,194,90,187,-174,-123,-180,-55,91,-16,66,47,113,-146,-200,154,-105,196,-159,156,139,-190,-137,-133,176,-57,-154,-107,-108,122,79,145,11,-22,140,123,-190,-113,20,20,15,-60,-71,-3,-192,-112,-47,159,134,122,81,85,-121,175,-150,-180,-61,129,-51,151,108,46,27,-9,-92,-68,15,146,115,-41,43,59,191,96,192,180,45,-38,110,-18,33,-162,68,146,-106,-69,-111,-92,-107,174,-164,9,-66,-25,66,-13,146,-97,-183,-82,172,-46,-154,179,31,-27,-35,194,-55,-121,181,-99,96,-107,-73,-63,2,-11,139,-81,38,155,25,69,179,-197,189,142,51,-186,74,-34,-37,-90,-129,125,120,145,74,-110,196,-178,-125,-112,-192,-3,-177,-34,-102,-53,184,117,85,-125,112,-180,-107,95,-105,-25,-121,-160,33,-72,-61,-143,101,-185,-45,64,42,160,36,45,121,-120,-13,-48,-147,-52,-173,-57,-63,-28,107,127,80,-155,93,88,-173,-49,-167,52,-134,148,164,170,94,-137,144,-174,-152,-34,-170,79,-49,116,-186,156,24,-24,-128,110,177,-100,176,-67,-52,-197,159,-127,-63,-62,-159,-94,-129,-6,-196,99,49,-114,-65,100,-194,2,-144,92,174,-53,-92,-125,-22,-26,52,192,-113,177,186,-40,-70,51,53,-184,-143,17,-103,62,141,-15,30,-125,-84,-59,43,71,-89,84,-25,125,-124,-116,135,-26,135,166,-143,-62,62,96,161,40,148,170,-26,85,-146,-147,-75,-53,-76,-9,-111,100,150,138,-42,101,103,181,-84,-57,-144,183,-62,-123,9,-35,-90,34,197,15,-137,-25,161,54,-44,-9,-21,-200,49,-171,-112,-199,-71,129,-91,61,-189,-199,-58,69,-73,-157,-111,146,-128,104,25,-165,36,-26,17,-94,121,-49,-189,48,-75,-180,138,170,-7,-182,34,51,3,21,-4,6,-19,-115,72,-7,-40,188,-177,14,-39,182,-10,-107,-42,-158,30,-156,-169,-163,62,-193,-42,-106,-182,-167,-17,141,146,-5,165,-22,-127,-134,60,-153,-168,-10,-63,181,-125,-189,52,-49,5,29,21,179,168,-173,-69,-157,118,-95,157,67,-58,116,18,74,-105,-46,-193,-138,138,43,-9,156,-16,107,171,166,40,-187,147,-113,103,12,-168,159,64,-133,41,-65,-2,-167,-188,-184,-195,127,-37,-80,-12,-80,-79,40,-26,-159,-178,-50,0,-75,5,71,-122,6,160,-98,190,-53,144,162,22,104,-88,45,88,82,-26,139,-173,-37,-200,28,186,-79,-116,71,199,92,-85,146,119,28,-131,68,-180,-129,34,177,45,-185,122,-150,161,164,27,-67,-140,-119,-105,-42,-37,13,-91,144,-42,26,-79,-105,196,191,-24,-25,50,-152,-126,42,157,89,13,22,32,-190,-125,-119,-36,-110,198,86,153,113,-53,188,-36,-6,-39,-115,-56,36,-54,-56,115,3,-109,85,-28,84,-21,-113,88,-197,-155,-153,132,-24,196,19,-40,-196,-96,-127,171,18,-114,-134,-89,-179,-168,187,0,22,-31,149,0,83,10,191,164,-40,18,-97,66,161,112,40,-187,-75,4,135,103,140,-108,166,129,-165,-189,76,-5,-168,-37,-147,-185,-161,92,-172,38,-7,-148,88,68,130,147,103,-87,90,125,-171,103,28,66,-89,154,184,-120,126,-144,161,-155,-104,-71,-77,-79,-189,131,112,41,-24,-5,55,-126,-150,158,-99,196,118,131,157,145,15,-82,62,-122,43,-9,-156,76,190,-153,143,-85,160,132,64,180,-8,-163,-179,109,-134,134,144,-5,-189,-119,26,-31,134,-125,34,-176,-43,-31,152,108,103,-43,-46,-87,197,-97,-133,-44,-175,102,-30,-125,130,-180,-141,78,66,117,75,-161,-166,85,-148,-19,-8,23,-24,-126,-46,-159,-12,114,106,28,27,118,-94,105,53];
console.log(threeSum(nums));
