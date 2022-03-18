price = int(input("enter your initial price"))
firstWeekP = price*1.1
secondWeekP = firstWeekP*1.05
thirdWeekP = secondWeekP*0.93
fourthWeekP = thirdWeekP*0.90
result = [firstWeekP, secondWeekP, thirdWeekP, fourthWeekP]
print(result)