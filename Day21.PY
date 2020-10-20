# Count number of letteres and digits in a string
def countsdigitleters(txt):
    spaceremoved = txt.replace(" ",'')
    countdigit = countletter = 0
    totalcounts = {}
    for i in spaceremoved:
        if i.isdigit() ==True:
            countdigit+=1
        else:
            countletter+=1
    totalcounts['DIGIT'] = countdigit
    totalcounts['LETTER'] = countletter