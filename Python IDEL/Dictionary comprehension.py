# Dictionary comprehension
keys=['a','b','c','d','e']
val=[1,2,3,4,5]
dic=dict(zip(keys,val))
print(dic)

mydic={x: x**2 for x in [1,2,3,4,5]}
print(mydic)
