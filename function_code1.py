import math
def paint_calculater(hieght,width,cover):
    Area=hieght*width
    num_of_corns=math.ceil(Area/cover)
    print(f"you will need {num_of_corns} cans 0f paint")
    
    
h =eval(input("Enter hieght  in meter "))
w=eval(input("Enter width in meter ")) 
coverage=7
paint_calculater(hieght=h,width=w,cover=coverage)   