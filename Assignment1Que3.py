inputNumbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
oddC = 0
evenC = 0
for x in inputNumbers:
    if not x % 2:
	    evenC+=1
    else:
        oddC+=1
print("Number of even numbers :",evenC)
print("Number of odd numbers :",oddC)
