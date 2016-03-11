aList = [1,2,3,4,5]#Using for loop
sum = 0
for i in range(5):
	sum = sum + aList[i]
print('Using for loop sum is:',sum)

s = 0
sum = 0
while s<len(aList):#Using for while loop
	sum = sum + aList[s]
	s = s + 1
print('Using while loop sum is:',sum)