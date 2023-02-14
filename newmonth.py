
month = input(" What month?")

if month == ('January' or "March" or "May"):
    print(f"{month} has 31 days")  
elif month == ("April" or "June"):
    print(f"{month} has 30 days")
elif month == "February":
    print(f"{month} has 28 days")


