# stris =  "LVIII"
# print(stris[0:len(stris):-1])
# I - 1
# V - 5
# X - 10
# L - 50
# C - 100
# D - 500
# M - 1000

class Solution1stversion:
    def romanToInt(self, s: str) -> int:
        total = 0
        s = s[::-1]
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                
                print(s[i])
                l = i+1
                current = s[i]

        return total
# #######################################
# #######################################
# #######################################


# below is working
# below is working
# below is working





class Solution2nd:
    def romanTo2nd(self,s):
        romandict = {
            'I': 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        current = 0
        nexti = 1
        totalint = 0
        while nexti<len(s):
            if romandict[s[current]]>=romandict[s[nexti]]:
                print('first half is',s[current],s[nexti])
                totalint+=romandict[s[current]]
                current+=1
                nexti+=1
            
            else:
                totalint+=romandict[s[nexti]]-romandict[s[current]]
                print('second half is',s[current],s[nexti])
                current+=2
                nexti+=2
        if len(s)==nexti:
            print('third half',s[nexti])
            totalint+=romandict[s[nexti-1]]
            
        print(totalint)

obj2 = Solution2nd()
print(obj2.romanTo2nd('MCMCCIV'))
# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.


# #######################################
# #######################################
# #######################################



# above is working 2nd
# above is working 2nd
# above is working 2nd
class solution3r:
    def roman3rd(self,s):
        romandict = {
            'I': 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        separet = []
        runningtotal = 0
        
        # s = s[::-1]
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                current= i
                next = j 
                if romandict[s[current]]>=romandict[s[next]]:
                    print(romandict[s[current]],romandict[s[next]])
                    runningtotal+=romandict[s[next]]
                else:
                    runningtotal = romandict[s[next]] - romandict[s[current]]
                    print(romandict[s[next]],romandict[s[current]])
        # print(runningtotal)

# obj3 = solution3r()
# print(obj3.roman3rd('MCMXCIV'))

