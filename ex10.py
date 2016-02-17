tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm\\ a \\ cat."
quote1 = "I am 6'2\" tall"# 将双引号字符串中的双引号转义
quote2 = 'I am 6\'2" tall.'#将单引号字符串中的单引号转义

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

big_cat = '''
I'm 
A
big
cat

'''
print (tabby_cat)
print (persian_cat)
print (backslash_cat)
print (fat_cat)
print (big_cat)
print ('%r'%(quote1))
print (quote2)