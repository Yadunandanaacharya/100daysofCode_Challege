# 1: 2 pointers
# Given a string s, find the length of the longest substring without 
# repeating characters.
# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
# Example 4:

# Input: s = ""
# Output: 0
 

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

#####################################
#####################################
#####################################

from collections import Counter
str1 = 'bbbb'
countis = Counter(str1)
# print(len(countis))
def repeastr(str1):
    if len(str1) == 0:
        return 0
    samestrs = Counter(str1)
    if len(samestrs) == 1 and countis[str1[0]] == len(str1):
        return 1
    j = 0
    substring = ''
    for i in range(0,len(str1)-1):
        if str1[i] != str1[i+1]:
            substring = substring + str1[i]
            i+=1
            print(substring)

print(repeastr('abcabcbb'))

#########################################
#########################################
# brute force

# stris = 'ABDEFGABEF'
# def repeatbrute(str1):
#     for i in range(0,len(str1)):
#         for j in range(i+1,len(str1)):
#             for k in range(j+1,len(str1)):
#                 print(str1[i],str1[j],str1[k])

# print(repeatbrute(stris))