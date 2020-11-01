def primes(lst):
    # primes = []
    if lst==1 or lst==0:
        print('Not prime')
    else:
        flag = 0
        for i in range(2,lst):
            if lst%i == 0:
                flag=1
                break
        if flag==1:
            print('Not')
        else:
            print('Prime')

# print(sum_primes([1,2,3,4,5,6,7,8,9,10]))
# print(primes(15))




def primes(lst):
    # primes = []
    if lst>1:
        for i in range(2,lst):
            if lst%i == 0:
                print('Not a prime')
                break
        else:
            print('prime')
    else:
        print('Not Prime')

# print(sum_primes([1,2,3,4,5,6,7,8,9,10]))
print(primes(4))




def primes_list(lst):
    primes = []
    for i in range(0,len(lst)):
        if lst[i]>1:
            flag = 0
            for j in range(2,lst[i]):
                if lst[i]%j == 0:
                    flag=1
                    break
            else:
                primes.append(lst[i])
                print('prime',lst[i])
        else:
            print('2 Not Prime',lst[i])
    return sum(primes)

# print(sum_primes([1,2,3,4,5,6,7,8,9,10]))
print(primes_list([1,2,3,4,5,6,7,8,9,10]))