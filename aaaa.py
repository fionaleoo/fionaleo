size = int(input('Masukkan besar bintang: '))

z = ''

def f(item):
    c = ''
    for item1 in range(size-item) :
        c += ' * '
    for item2 in range(item) :
        c += '   '
    for item3 in range(item-1) :
        c += '   '
    for item4 in range(size-item) :
        c += ' * '
    c += '\n'
    return c

for i in range((size*2)-1): 
    z+= ' * '
z+='\n'
for item in range(1, size):
    z += f(item)
for item in range(size-2,0,-1):
    z += f(item)
for i in range((size*2)-1): 
    z+= ' * '
z+='\n'
print(z)