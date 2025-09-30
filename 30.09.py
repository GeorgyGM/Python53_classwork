min1=int(input("введите начало диапазона 1"))
max1=int(input("введите начало диапазона 1"))
min2=int(input("введите начало диапазона 2"))
max2=int(input("введите начало диапазона 2"))
min3=int(input("введите начало диапазона 3"))
max3=int(input("введите начало диапазона 3"))
n = int(input("введите число"))
if min1>max1:
    min1,max1=max1,min1
if min2>max2:
    min2,max2=max2,min2
if min3>max3:
    min3,max3=max3,min3

counter=0
if min1<=n<=max1: counter+=1
if min2<=n<=max2: counter+=1
if min3<=n<=max3: counter+=1

print(counter)
