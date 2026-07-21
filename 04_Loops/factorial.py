num=int(input("Enter a number:"))
factorial=1
if num<0:
    print("Factorial doesn't exist for negative numbers.")
elif num==0:
    print("Factorial for 0 is 1")
else:
    for i in range (1, num+1):
        factorial*=i
    print(factorial)
print()
