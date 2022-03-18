print("Enter your initial price")
price = int(input())
def applyDiscount(coefficient) :
   return coefficient*price
    
discounts = [1.1, 1.05, 0.93, 0,90]
result = map(applyDiscount, discounts)
print (list(result))