
month = input(" What month do you want to investigate?")

Knuckle = ["January","March","May","July","August","October","December"]

Dip = ["April","June","September","November"]

if month in Knuckle:
    print(f"{month} has 31 days")
elif month in Dip:
    print(f"{month} has 30 days")
elif month == "February" :
    print(f"{month} has 28 days")
else:
    print(f"{month} is not a month")