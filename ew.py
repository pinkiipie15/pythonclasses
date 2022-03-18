print ("please enter your list")
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
value = int(input("please enter your number"))
if value > 0 :
    print("resault:", a + b)
else:
    print ("resault:", b + a)

print (a)