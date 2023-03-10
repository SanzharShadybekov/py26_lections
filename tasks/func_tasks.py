"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""

"""
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
"""
"""
Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
"""

# 2)

# ---------------------------------------------------------------
"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.  

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used: 

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
"""
"""
Input: s = "III"
Output: 3
Explanation: III = 3.

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""
# def romanToInt(s: str) -> int:
#     dict_ = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
#     s = list(s)
#     newlist=[]
#     for i in s:
#         num = dict_[i]
#         newlist.append(num)
#     list1 = newlist[::-1]
    
#     i = 0
#     last = list1[0]
#     for x in list1:
#         if x < last:  
#             i -= x
#         else:
#             i += x
#         last = x
#     return i
    
# print(romanToInt("III"))
# print(romanToInt("LVIII"))
# print(romanToInt("MCMXCIV"))
# print(romanToInt("MMXCV"))

"""
Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string."""
"""
Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.
"""

"""
Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: false
"""
"""
Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
Output: true
"""
def compare_to_arrays(word1, word2):
    from functools import reduce
    oper = reduce(lambda x, y:(x+y), word1)
    oper1 = reduce(lambda x, y:(x+y), word2)
    if oper == oper1:
        return True

    else:
        return False

print(compare_to_arrays(["a", "cb"],["ab", "c"] ))
print(compare_to_arrays(["abc", "d", "defg"],["abcddefg"] ))