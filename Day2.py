# def stutter(word):
# 	return word[:2] +'... ' + word[:2] + '... '+ word'?'

# print(stutter('increasing'))

def su(lst):
    sum = 0
    for i in lst:
        if type(i) == int:
            sum = sum + i
    return sum

print(su([1,2,'hi']))
