

l = [1,2,3,4]

l.append(5) # them vao cuoi mang
print(l)


l.insert(0,100)
print(l) # them vao vi tri chi dinh



print(l.count(1)) # in ra so lan xuat hien cua phan tu do

l.reverse() # dao nguoc mang

print(l)

l.remove(100) # xoa phan tu dua vao gia tri
print(l)

for _ in range(10,50,10):
    print(_)


# tạo một list nhanh
ll = [x for x in range(10)]


ll2 = [x**2 for x in range(10)]


ll3  = [x**2 for x in range(10) if (x%2)==0]


ll4  = [x**2 if (x%2)==0 else 5 for x in range(10) ]


# tạo mảng full 0

zeros=[0]*5
# nối mảng
arr = [1,2]+[3,4]

# loop 2 mảng

for a,b in zip(range(3),range(4)):
    print(a,b)


# tuple
list2d = [(a,b)for a,b in zip(range(3),range(4,7))]

print(list2d)

# dictionary
list2dKeyvalue = [{a:b} for a,b in zip(range(3),range(4,7))]

print(list2dKeyvalue)

# tạo mảng 2 d
l2d = [[a,b] for a,b in zip(range(3),range(4,7))]

print(l2d)

print(arr)
print(zeros)
print(ll4)

