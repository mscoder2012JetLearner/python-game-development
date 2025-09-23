tuple=("max","coedpoeth","wrexham","wales","graet Britan","europe")
for i in tuple:
    print(i)

n,v,ci,co,gb,cont=tuple

print(n)

numbers=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25)

print(numbers[6])

# numbers[6]=60
#immutable(can't change it)

#numbers.append(100)
#can't change

print(numbers[6:15:2])

for i in range(100):
    print("a tuple in a tuple in")

tuple1=("yugu",[2,1,4,3,],("tryr","fyfsu"))
print(tuple1[2][0])

tuple2=(((((((((("!"))))))))))
print(tuple2[0][0][0][0][0][0][0][0][0])

tuple1[1][2]=40
print(tuple1[1][2])