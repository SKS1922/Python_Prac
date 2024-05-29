n = int(input("Enter value of n: "))
factorial=1
if n<0:
    print("Enter a positive number")
elif n==1 or n==0:
    print("The factorial is:1")
else:
        for i in range(1,n+1):
            factorial=factorial*i
        print("The ans of factorial is:",factorial)