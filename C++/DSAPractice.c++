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
