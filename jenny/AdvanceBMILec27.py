weight =eval(input("Enter weight : "));
height=eval(input("Enter height : "));
bmi=round(weight/height**2);
if bmi<=18.5:
    print(f"Your bmi is {bmi} and you are undetweight");
elif bmi <25:
    print(f"Your bmi is {bmi} and you  have normal weight");
elif bmi <30:
    print(f"Your bmi is {bmi} and you  are over weight");
elif bmi <35:
    print(f"Your bmi is {bmi} and you are obes");
else:
    print(f"Your bmi is {bmi} and you are clinically obes")