# ["g", "e", "o"], [1, 0, 2]
words = ["g", "e", "o"]
posi = [1, 0, 2]
newIndex = []
def correct_word_with_index(words,posi):
    new_word = ''
    for j in posi:
        new_word = new_word + (words[j])
    return str(new_word)

#   print(correct_word_with_index(words,posi))



# Given an unsorted array of nonnegative integers, find a continuous
#  subarray which adds to a given number.
# Input: arr[] = {1, 4, 20, 3, 10, 5}, sum = 33
# Ouptut: Sum found between indexes 2 and 4
# Sum of elements between indices
# 2 and 4 is 20 + 3 + 10 = 33

# This is simple example question is different
# https://practice.geeksforgeeks.org/problems/subarray-with-given-sum/0

def sum_indexes(arrays,finalsum):
    sumi = finalsum
    sumis = []
    for i in range(len(arrays)):
        sumi = sumi - arrays[i]
        print(sumi)
    #     sumis.append()
    #     if sumi == finalsum:
    #         print(sumis)
    # return sumis
# print(sum_indexes([1, 4, 20, 3, 10, 5],33))

arrayis = [1, 4, 20, 3, 10, 5,7,90,56,4]
sumis = 33
s = 0
for i in range(0,len(arrayis)):
    for j in range(i+1,len(arrayis)):
        for k in range(j+1,len(arrayis)):
            s = s + arrayis[i]+ arrayis[j] + arrayis[k]
            if s == sumis:
                sumis = 33
                # print(i,j,k)





def sum_index(arr,sumi):
    
    sumis = 0
    start = 0
    for i in range(0,len(arr)):
        while sumis>sumi and start<i-1:
            sumis = sumis-arr[start]
            # print(sumis,i, start)

            start+=1
        if sumis==sumi:
            print(start,i-1)
            # return 1
       
        sumis = sumis + arr[i] 
        
       
    # return 0
print(sum_index([1, 4, 20, 3, 10, 5,7,90,56,4],33))