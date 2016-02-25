import time
def foo():
	print('in foo()')
#定义一个计时器，传入一个，并返回另一个附加了计时器功能的方法
def timeit(func):
#定义一个内嵌的包装函数，给传入的函数加上计时功能的包装	
	def wrapper():
		start = time.clock()
		func()
		end = time.clock()
		print('used:',end-start)

	return wrapper

foo = timeit(foo)
foo()