nterm=int(input("Enter the value:"))
num1,num2=0,1
count=0
if nterm<=0:
    print("Give me another value")
elif nterm==1:
    print(num1)
else:
    while(nterm>count):
        print(num1)
        nth=num1+num2
        num1=num2
        num2=nth
        count+=1