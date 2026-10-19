print("Enter a number for the numerator: ")
num1 = int(input())
print("Enter a number for the denominator: ")
num2 = int(input())

if num1%num2 == 0:
    print("\n" +str(num1)+ " is divisible by "+str(num2))
else:
    print("\n" +str(num1)+ " is not divisible by "+str(num2))