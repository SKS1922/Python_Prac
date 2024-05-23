m=float(input("Math mark is:"))
p=float(input("Physics mark is:"))
c=float(input("Chemistry mark is:"))
total_mark=m+p+c
if m>=65 and p>=55 and c>=50:
    print("You are eligible for admission")
elif total_mark>=180:
    print("You are eligible for admission")
elif m + p>=140:
        print("You are eligible for admission(combined math and physics mark)")
else:
    print("You are not eligible for admission")