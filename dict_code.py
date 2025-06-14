student_data={
    'ram':{'roll_no':100,"age":19,'subject':'python'        
    },
    "shyam":{'roll_no':102,'age':20,"subject":'java'        
    },
    "avadhesh":{
        'roll_no':103,'age':20,'subject':'mysql'
    }
}
print(student_data)
del student_data['shyam']
print(student_data)
print('delete : ', student_data.pop('avadhesh'))
print(student_data)

print("     ...... X********list_dict********x ..................")


student_data=[
    {"ram":"'roll_no':100,'age':19,'subject':'python'  "      
    },
    {'shyam':"'roll_no':102,'age':20,'subject':'java' "      
    },
    {
        'roll_no':103,'age':20,'subject':['mysql','java']
     }
    ]
print(student_data)
del student_data[0]
print(student_data)
print(student_data[1]['subject'])