c=float(input("Celcious is:"))
if c<0:
    print("Freezing Weather")
elif c>0 and c<=10:
    print("Very Cold Weather")
elif c>10 and c<=20:
    print("Cold Weather")
elif c>20 and c<=30:
    print("Normal in Temp")
elif c>30 and c<=40:
    print("It's Hot")
else :
    print("It's Very Hot")