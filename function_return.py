def add(a,b):
    c=a+b
    
    return c

def format_name(first,last):
    farst_name=first.title()
    last_name=last.title()
    return f"{farst_name} {last_name}"

x=input("Enter first name: ");y=input("Enter second name: ")
z=add(7,9)
print(z)

formated_name=format_name(first=x,last=y)

print(formated_name)

