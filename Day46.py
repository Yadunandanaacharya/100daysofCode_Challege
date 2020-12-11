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

def dupli(str1):
    string = str1
    counteach = Counter(string)
    value = list(counteach.values())
    repeat = [i for i in value if i>1]
    if repeat != []:
        return True
    else:
        return False
def repeastr(str1):
    if len(str1) == 0:
        return 0
    samestrs = Counter(str1)
    if len(samestrs) == 1 and countis[str1[0]] == len(str1):
        return 1
    j = 0
    substring = ''
    mainarr = []
    lensubstr = 0
    for i in range(0,len(str1)):
        substring = substring + str1[i]
        repeatcheck = dupli(substring)
        if repeatcheck == True:
            substring =(substring[1:])
        mainarr.append(substring)
    return max([len(i) for i in mainarr])    

print(repeastr('abcabcdbb'))

#########################################
#########################################
# brute force



# def repeatbrute(str1):
#     for i in range(0,len(str1)):
#         for j in range(i+1,len(str1)):
#             for k in range(j+1,len(str1)):
#                 print(str1[i],str1[j],str1[k])

# print(repeatbrute(stris))



# optimized prime checker:
def primeornot(n):
    if n>1:
        for i in range(2,int(n/2)):
            if (n%i) == 0:
                print('Not prime')
                break
            else:
                print('prime')
               
    else:
        print('Not prime')
        

# print(primeornot(121))