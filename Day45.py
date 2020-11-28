# 2 sum with 2 pointer
# Only works on sorted array
def sum2(arr1,target,n):
    i = 0
    j = n-1
    while i < j:
        if arr1[i] + arr1[j] == target:
            return [i,j]
        elif arr1[i] + arr1[j] > target:
            j -= 1
        else:
            i += 1
    return 0






arr1 = [1,2,2,3,5,6]
n1 = len(arr1)
target1 = 11

arr2 = [2,3,4]
n2 = len(arr2)
target2 = 6

arr3 = [3,3]
n3 = len(arr3)
target3 = 6
obj1 = sum2(arr1,target1,n1)
print(obj1)