a = int(input("Enter a value for a THAT IS LESS THAN 100: "))
b = int(input("Enter a value for a THAT IS LESS THAN 100: "))
c = int(input("Enter a value for a THAT IS LESS THAN 100 (i know it's repetative just deal with it): "))

avg = (a+b+c) / 3
print("avg = ", avg)

if avg > a and avg > b and avg > c:
    print("%d is higher than %d, %d, %d"%(avg, a, b, c))

elif avg > a and avg > b:
    print("%d is higher than %d, %d"%(avg, a, b))

elif avg > a and avg > c:
    print("%d is higher than %d, %d"%(avg, a, c))

elif avg > b and avg > c:
    print("%d is higher than %d, %d"%(avg, b, c))

elif avg > a and avg > b and avg > c:
    print("%d is higher than %d, %d, %d"%(avg, a, b, c))

elif avg > a:
    print("%d is higher than %d,"%(avg, a))

elif avg > b:
    print("%d is higher than %d"%(avg, b))
elif avg > c:
    print("%d is higher than %d"%(avg, c))
else:
    print("Invalid input")