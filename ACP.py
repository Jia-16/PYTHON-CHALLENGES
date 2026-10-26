rice = 12
milk = 4
fruit = 8
total1 = 0
baskets = 2
familyMembers = 4

total1 = (rice + milk + fruit) / 4
print("(Cost per person: rice + milk + fruit) / 4 = ", total1)

totalItem = int(input("What is the total number of items you have? "))
totalPeople = int(input("How many people you have in your beautiful life to share the food with? "))

shared = totalItem / totalPeople
if totalPeople == 0:
    print("You CAN'T BE SERIOUS! that is stastically impossible.")
else:
    if totalItem % totalPeople == 0:
        print("The items can be shared equally.")
        print("Each person gets", totalItem // totalPeople, "items.")
    else:
        print("The items cannot be shared equally.")
        print("The remainder is", totalItem % totalPeople)

avg = 65
totalWeeks = 4
wrongWeekCost = 50
correctWeekCost = 80

total2 = avg * totalWeeks
correctAvg = correctWeekCost / totalWeeks

print("Earlier average = 65, but the correct average is ", correctAvg)

store_a_average = 70
store_b_average = 75
store_c_average = 80

verdict = store_a_average < store_b_average and store_b_average < store_c_average

print(verdict)


print("Basket cost per person:", baskets)
print("Corrected average:", correctAvg)
print("Verdict:", verdict)