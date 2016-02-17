x = "There are %d types of people." %10 #字符串包含字符串
binary = 'binary'
do_not = "don't"
y = "Those who know %s and those who %s."%(binary,do_not)#字符串包含字符串

print (x)
print (y)

print ("I said: %r."%x)#字符串包含字符串
print ("I also said:'%s'."%y)#字符串包含字符串

hilarious = False
hilariou = True
joke_evaluation = "Isn't that joke so funny?! %r"

print (joke_evaluation %hilarious)
print (joke_evaluation %hilariou)
w = "This is the left side of..."
e = "a string with a right side."

print (w+e)