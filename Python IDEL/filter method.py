from functools import *
#filter
a=[1,2,3,4,5]
fil=list(filter(lambda x: x%2==0,a))
print(fil)

#map
fi=list(map(lambda x:x*x,a))
print(fi)

#reduce
f=reduce(lambda x1,x2: x1+x2,fi)
print(f)
