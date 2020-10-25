# # Reverse a string wthout using any inbuitl function
# def reversestring(txt):
#     string = ''
#     for i in range(len(txt)-1,-1,-1):
#         string = string + txt[i]
#     print(string)
#     reve = ''.join([txt[i] for i in range(len(txt)-1,-1,-1)])
#     print(reve)
# print(reversestring('Hai'))

# def is_palindrome(txt):
# 	return ''.join([txt[i] for i in range(len(txt)-1,-1,-1)]) == txt
	

def fibonacci(n):
    if n==0 or n==1:
        output = 1
        # print('1',output)
        return output
    else:
        output = n + fibonacci(n-1)
        # print('2',output)
        return (output)

# print(fibonacci(10))


def fibis(n):
    start = 1
    end = 2
    for i in range(0,n):
        if i<=2:
            # Write whatever here
            i='hai'
        else:
            next = start + end
            start = end
            end = next
    return (str(next))
print(fibis(10))


def fibis(n):
    first = 1
    second = 2
    for i in range(0,n):
        if i==1 or i==2 or i==0:
            # Write whatever here
            i='hai'
        else:
            next = first + second
            first = second
            second = next
    return (str(next))
# print(fibis(10))