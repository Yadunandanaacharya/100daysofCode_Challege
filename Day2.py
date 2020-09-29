# def stutter(word):
# 	return word[:2] +'... ' + word[:2] + '... '+ word'?'

# print(stutter('increasing'))

def su(lst):
    sum = 0
    for i in lst:
        if type(i) == int:
            sum = sum + i
    return sum

# print('SUM IS {}'.format(su([1,2,'hi'])))

# print('Numbers are {}'.format(i))
import sys
def add_up(num):
    if len(num) == 0:
        return ""
    
    else:
        return add_up(num[1:]) + num[0] 

# print('num is',add_up('hello'))
obji = 'hello'
print(obji[-2:])