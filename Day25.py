# Armstrong number:
n =123
# print(123//10)
# print(12//10)
# print(1//10)
count = 0
digit = 0

while n!=0:
    n = n//10
    # digit = digit%10
    # print(digit)
    count+=1

# print(count)
# print(123%10)
# print(12%10)
# print(1%10)

def armstrong_num_or_not(nis):
    nfrom_function = nis
    nis = nis
    digitis =nis
    countis = 0
    armstrong = []
    armstrongis = 0
    while nis!=0:
        digitis = nis%10
        nis = nis//10
        countis+=1
        armstrong.append(digitis**count)
        armstrongis = armstrongis+ (digitis**count)
    if armstrongis == nfrom_function:
        return "Armstrong"
    else:
        return "Not"


# print(armstrong_num_or_not(153))
# Simple logic: counting digits of integer with "//" logic
# getting single digits separately 3 in one loop 5 in another loop 1 last 
# example with "%" logic.


# Prime or not:
n=10

if n<1 or n==1:
    print("Not prime")
else:
    flag = 0
    for i in range(2,n//2):
        if n%i==0:
            flag=1
            break
    print(flag)
    if flag==1:
        print('Not ')
    else:
        print("prime")


# Don't remember codes or byheart them, try to underastand logic
# and try to remember logic
# In case of deteceting prime integers, if numbers are less than 0 and 1then 
# not prime or else, if number is divisible in the range of 2 to number//2
# means if 10 is the number then cheking range from
# 2 to 5 because you know that right above half of integer there won't be any 
# integer which divides that number.



def fib(n):
    first = 1
    second = 2
    for i in range(n):
        if i<=2:
            i = n
        else:
            total = first+second
            first = second
            second = total
    return total
# print(fib(10))