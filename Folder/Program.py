x = int(input("Introduceti un numar: "))
bitNumber = 2


print((x >> bitNumber) & 1)

'''
if((x >> bitNumber) & 1):
    print(x)
else:
   x = x|(1<<bitNumber)
print(x)
'''

''''
if((x >> bitNumber) & 1):
    x = x & ~(1 << bitNumber)
    print(x)
else:
    print(x)
    '''