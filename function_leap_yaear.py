def leap_year(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False        
        else:
            return True    
    else:
        return False
def day_in_month(year,month):
    day_list=[31,28,31,30,31,30,31,31,30,31,30,31]
    if leap_year(year) and month==2:
        return 29
    else:
        return day_list[month-1]
    
year=int(input("Enter year : "))
month=int(input("Enter month in number : ")) 
day=day_in_month(year,month)
print(f"Year ({year})in month day is {day} ")  