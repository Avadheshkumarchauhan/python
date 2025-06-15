# Identity oprater 
# is and is not oprater

a=5;
b=5;
print(id(a),id(b));
print(a is b);
print(a is not b);#false because addresh of a equal addresh of b
c='5'
print(id(c));
print(a is c);
print(" a==c ",a==c)
l1=[1,2,3,4];
l2=[1,2,3,4];
print(id(l1),id(l2));
print(l1 is l2);
print(l1 is not l2);
name="avadhesh";
nickName="avadhesh";
print(id(name),id(nickName));
print(name is nickName);
a=8;
print(a,id(a));
print(a is a);