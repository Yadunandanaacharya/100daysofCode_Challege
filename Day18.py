
lst = ['hai','baai','seeus','sai']
for i in range(len(lst)):
    print('1',lst[i])
    for j in range(i+1,len(lst)):
        if len(i) > len(j):
            lst[i] = lst[j]
            