# # Count number of letteres and digits in a string
# def countsdigitleters(txt):
#     spaceremoved = txt.replace(" ",'')
#     countdigit = countletter = 0
#     totalcounts = {}
#     for i in spaceremoved:
#         if i.isdigit() ==True:
#             countdigit+=1
#         else:
#             countletter+=1
#     totalcounts['DIGIT'] = countdigit
#     totalcounts['LETTER'] = countletter

def oldest(people):
	keysare = list(people.keys())
	valuesare = list(people.values())
	maxvalueindex = valuesare.index(max(valuesare))
	return keysare[maxvalueindex]
# Which returns name of oldest person's age
# Test.assert_equals(oldest({'Charlotte': 53, 'Oliver': 15, 'Henry': 18, 'Gabriel': 46, 'Violet': 13}), "Charlotte")
print(oldest({'Charlotte': 53, 'Oliver': 15, 'Henry': 18, 'Gabriel': 46, 'Violet': 13}))

# Best Solution from edabit:
# def oldest(people):
# 	return max(people, key=people.get)



def sum_fractions(lst):
	sumis = 0
	for i in range(len(lst)):
		insidelist = lst[i]
		first_element = insidelist[0]
		second_elemenet = insidelist[1]
		fraction = first_element/second_elemenet
		sumis = sumis + fraction
	return (round(sumis))
	
# Single line code found in edabit site:
def sum_fractions(lst):
	return round(sum([x[0]/x[1] for x in lst]))



# Reversing two words in a string
def name_shuffle(txt):
	space_split = (txt.split(" "))
	return " ".join(space_split[::-1])
# Test.assert_equals(name_shuffle("Donald Trump"),"Trump Donald")
