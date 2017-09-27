a = [1, 2, 3, 4, 5]

highest = a[0]
for i in range (1, len(a)):
	if(highest < a[i]):
		highest = a[i]
print(highest)
