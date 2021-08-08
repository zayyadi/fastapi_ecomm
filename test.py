def rot(a, d):
    b = []
    for i in range(-d,len(a)):
        b.append(a[i])
    b.extend(a[0:d])
    return b

rot([1,2,3,4,5,6,7],3)
rot([3,4,6,7,8,9,10,23], 2)
print(list('rot'))
