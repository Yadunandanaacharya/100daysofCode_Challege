listis = ["flower","flow","flight"]
both = ''
from collections import Counter
li = [j for i in listis for j in i]
d = dict(Counter(li))
for key,value in d.items():
    if value==len(listis):
        both=both+key
# print(both)
# for i in listis[0]:
#     for j in listis[1]:
#         for k in listis[2]:
#             if i or j or k in both:
#                 continue
#             else:
#                 if i==j and i==k:
#                     both = both + i + j + k
# print(both)


# ###########second try
# ###########second try
# ###########second try
# ###########second try
list2 = ["flower","flow","flight"]
multi_list = [["flower"],
              ["flow"],
              ["flight"]]

class solution2:
    def repeated(self,str1,str2):
        first_word = str1
        second_word = str2
        result = ''
        n1 = len(first_word)
        n2 = len(second_word)
        i = 0
        j = 0
        while i <= n1-1 and j <= n2-1:
            if first_word[i] != second_word[j]:
                break
            result += first_word[i]
            i += 1
            j += 1
        return (result)

    def outerfunction(self,listis):
        if listis != []:
            comparing_string = listis[0]
            for i in range(1,len(listis)):
                comparing_string = self.repeated(comparing_string,listis[i])
            return comparing_string
        return ''

obj2 = solution2()
print(obj2.outerfunction([]))
