n=int((input("n is:")))
i=1
sum=0
while i<=n:
    if i%2==0:
        sum=sum+i
    i+=1
print("The sum of the even num is:",sum)
