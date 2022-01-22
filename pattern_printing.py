#------------------------pattern printing-----------------------
#When the value of Boolean is 1 i.e. True, the pattern will be printed as shown above.
#But if the value of Boolean is 0 or false, then the triangle will be printed upside down.
print("How Many Row You Want To Print")
one= int(input())
print("Type 1 Or 0")
two = int(input())
new =bool(two)
if new == True:
    for i in range(1,one+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
elif new ==False:
    for i in range(one,0,-1):
        for j in range(1,i+1):
            print("*", end="")
        print()
