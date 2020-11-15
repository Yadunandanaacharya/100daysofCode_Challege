
    # def reverse(self, x):
    #     intmod10 = x % 10
class Solution(object):
    def reverse(self,x):
        if (2**31) <= x <= (2**31)-1:
            if x > 0 :
                divide = x
                revstr = ''
                while divide>0:
                    revstr = revstr + str(divide%10)
                    divide = divide//10
                if revstr[0] == '0':
                    return int(revstr[1:])
                else:
                    return int(revstr)
            elif x < 0 :
                x = 0 - x
                divideis = x
                revstris = ''
                while divideis>0:
                    revstris = revstris + str(divideis%10)
                    divideis = divideis//10
                return 0 - int(revstris)
        else:
            return 0
        

obj = Solution()
print(obj.reverse(123))



       
# In every iteration divide will get less number like 321->32->3->0
# So you need to add this revstr, previously I added num to the revstr
# But I was not dividing num by anything, so it was not reversing
# This is leetcode problem 
    # print(321//10)
    # print(32//10)
    # print(3//10)
    # revstr = ''
    # revstr = revstr+str(321%10)
    # print(revstr)
    # revstr = revstr+str(32%10)
    # print(revstr)
    # revstr = revstr+str(3%10)
    # print(revstr)





# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21
# Example 4:

# Input: x = 0
# Output: 0
def reveis(num):
    num = num
    reve = ''
    while num>0:
        reve = reve + str(num%10)
        num = num//10
    print(reve)


# hh = '021'
# if hh[0]:
#     print(hh[1:])
# print((2**31)-1534236469)


# #####################################################
# #####################################################
# #####################################################
# #####################################################
# Working Solution
class Solution:
    def reverse(self, x) -> int:
        x= int(str(x)[::-1]) if x >=0 else -int(str(-x)[::-1])
        return x if x < 2147483648 and x >= -2147483648 else 0;