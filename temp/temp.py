"""
words = keys
numeric symbols = values
"""
# these 2 are pretty much the same : dict()-> convert () into a dict
print(dict([('two', 2), ('one', 1), ('three', 3)]))
print(dict(one=1, two = 2, three = 3))
# can be applied on a partial dict
print(dict({'one': 1, 'three': 3}, two=2))

# zip to match the indices of 2 lists
e = (dict(zip(['one', 'two', 'three'], [1, 2, 3])))
print(e)

print()
# list(dict) -> return a list of all the keys ['one', 'two', 'three']
# len(dict) -> return number of items in dict:
# e.g.
print(len(e))
