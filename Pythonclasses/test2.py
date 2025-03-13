# return statement in function
'''def addNUm(num1, num2):
    return num1 + num2
num = addNUm(5.5,4.5) # saves  this one
print(num)
print(addNUm(10,8)) # does not save this one

# ternary operation
def seacrhList(y, x):
    return True if x in y else False
result = seacrhList(['one', 2, 'three'], 'four')
print(result)'''

# scope in function scope is like declaring a varible
# 1. global scope:
#num = 55 # this is a global scope does not work in a function
'''def scope():
    num += 1
scope()'''

# 2. function scope: a variable that works with in a function block only
'''def test():
    w = 'testing'
    return w
valu = test()
print(valu)
print(w)''' # this will give an error
# 3. classes scope:

# in place algorithm
'''sports = ['basketball', 'volley', 'table tennis', 'football']
def chSports(csp):
    csp[2] = 'cricket'
print(f'before changing: {sports}')
chSports(sports)
print(f'after changing: {sports}')'''








