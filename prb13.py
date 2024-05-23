total_days=int(input("Enter the days:"))
years=int(total_days/365)
remaining=total_days%365
weeks=int(remaining/7)
days=remaining%7
print(years,"years",weeks,"weeks","and",days,"days")