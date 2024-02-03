def adder(*args):
    newList = []
    for i in args:
        newList.append(i)
    return newList
lst1 = [1, 2]
lst2 = [3, 4]
lst3 = [5, 6]
lst4 = [lst2, lst3]
lst1 = adder(*lst4)
print(lst1)

#5. Longest Palindromic Substring
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        Max_Len=1
        Max_Str=s[0]
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                if j-i+1 > Max_Len and s[i:j+1] == s[i:j+1][::-1]:
                    Max_Len = j-i+1
                    Max_Str = s[i:j+1]

        return Max_Str

#6. Zigzag Conversion
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        inc = 2 * numRows - 2
        n = len(s)

        result = ""

        for i in range(min(n, numRows)):
            result += s[i]
            # right_i is the actual index of
            # the char on the vertical line
            # right_i = inc + i | left_i = (inc + i) - 2*i
            left_i, right_i = inc - i, inc + i

            while left_i < n:
                # If it is not the first or last row
                if i != 0 and i != numRows - 1:
                    result += s[left_i]
                # If right_i is still a valid index
                if right_i < n:
                    result += s[right_i]

                left_i += inc
                right_i += inc
