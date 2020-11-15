# Palindrome without converting to string
def pali(num):
    reveris = []
    while num != 0:
        reveris.append(num % 10)
        num = num // 10
    print(int(reveris))

# print(pali(123))




# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Anangram or not:
class Solution1:
    def isAnagram(self, s, t):
        print('Hai')    
# obj1  = Solution1()
# print(obj1.isAnagram('anagram','nagaram'))