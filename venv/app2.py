#x = [4.1,	6.5,	12.6,	25.5,	29.8,	38.6,	46,	    52.8,	59.6,	66.3,	74.7]
#y = [2.2,	4.5,	10.4,	23.1,	27.9,	36.8,	44.3,	50.7,	57.5,	64.1,	72.6]
import math

x = [30, 25, 20, 15, 10]
y = [0, 0, 0, 1, 1]

N = len(x)
xsum = sum(x)
ysum = sum(y)

def sumofprod(list1, list2):
    sum_ = 0
    for i in range(len(list1)):
        sum_ += list1[i] * list2[i]
    return sum_

xysum = sumofprod(x, y)
x2sum = sumofprod(x, x)
y2sum = sumofprod(y, y)

m = ( (N*xysum) - xsum*ysum ) / ((N*x2sum) - (xsum*xsum) )
b = ( (x2sum*ysum) - xsum*xysum ) / ((N*x2sum) - (xsum*xsum))

x_ = float(input("Temperature >>  "))
y_ = m * x_ + b

up = N*xysum - xsum*ysum
r2 = (up*up) / ((N*x2sum - xsum*xsum) * (N*y2sum - ysum*ysum))

print("value of y: ", y_)
print("value of r2: ", r2)


if y_ >= 0:
    print("\nYou should wear a jacket")
else :
    print("\nYou don't have to wear a jacket")