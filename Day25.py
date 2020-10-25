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
for i in range(1,n):
    if n%i==0:
        print("Not Prime")
    else:
        if n//1==0 and n//n==0:
            print("prime")