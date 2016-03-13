#get filename
import os
fname = input('Enter filename:')
print()

#attempt to open file for reading
if os.path.exists(fname):
	fobj = open(fname,'r')
	for eachLine in fobj:
		print (eachLine)
else:
	print('File not exist')