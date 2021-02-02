#string data type
a='string'
print(a)
print(type(a))
#int data type
b=100
print(b)
print(type(b))
#float date type
c=1.23
print(c)
print(type(c))
#complex data type
d=1+6j
e=2-3j
print(d,e)
print(type(d),type(e))
#list data type
lis=[1,2,3,4,5,6,'list']
print(lis)
print(type(lis))
#tuple dtat type
tup=(1,2,3,4,'tuple')
#duplicates are not allow
print(tup)
print(type(tup))
#range data type
for i in range (0,100,10):
    print(i)
#mapping type
dic=dict(name='ram',age=30)
print(dic)
print(type(dic))
#set types
sets={1,23,4,5,6,7,8,9}
print(sets)
print(type(sets))
#boolean type
bool=True
print(bool)
print(type(bool))
#bytes types
byte=b'hello'
print(byte)
print(type(b))
#bytearray type
x=bytearray(6)
print(x)
print(type(x))
#memoryview
z=memoryview(x)
print(z)
print(type(z))
