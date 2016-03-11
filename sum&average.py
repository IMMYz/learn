a = [1,2,3,4,5]
sum = 0
print('1:sum(1-5)\n2:average(1-5)')
c = int(input('1 or 2\n'))
if c == 1:
	for i in a:
		sum = sum + i
	print('sum = ',sum)
elif c == 2:
	for i in a:
		sum = sum + i
	print('average = ',(sum/i))