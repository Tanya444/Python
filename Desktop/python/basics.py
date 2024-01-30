# Variables,Datatypes(int,str,float,bool,NoneType),Operators(arithmetic-+*/%**,comparison,logical-and,or,not)
"""
/ always give floating value,ternory operator ?: not work in python->use one liner if else
identifier cant start with digit and do not contain special symbols.
input() always take string as input, else you need to typecast.
"""
x,y="tanya ","arya"
print(x+y)
ans=print("yes") if 20>3 else print("no")
print(90-45)
name=input("Enter your name:")
age=24
price=25.99
flag=True
a=None
print(type(name))
print(type(age))
print(type(price))
print(type(flag))
print(type(a))
a=4
b=2
print(a/b)
print(a%b)
print(a**b)
print(True==False)
print(True!=False)
print("Is not 70 greater than 60", not(70>60))
#type conversion(implicit to superior datatype by interpretor),type casting(manually)
a=6
b=6.5
c="6"
sum=a+b
print(sum)
print(int(c)+a)
print(int(c)+b)
#taking multiple inputs from user
'''
age,colour=input("enter your age and favorite color\n").split(",")
print(age)
print(colour)
'''
