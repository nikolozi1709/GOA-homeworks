# 1 comparison operators
num1 = int(input("Enter any number"))
num2 = int(input("Enter any number"))
print (num1>num2)
print (num1<num2)
print (num1==num2)
#2 
num_1 = int("10")
num_2 = int("15")
num_3 = int("20")
num_4 = 10
num_5 = 12
print (num_1*num_2*num_3*num_4*num_5/5)
#3
name_1 = input ("Enter your name")
name_2 = input ("Enter your name")
name_3 = input ("Enter your name")
amount = int(input("Enter any number"))
print (name_1+name_2+name_3)
print ((name_1+name_2+name_3)*amount)
#4 
#ჩვენ ვისწავლეთ logical operators   რომლებიც აფასებენ ლოგიკურ გამოსახულებებს გამოყენებული ფუნქციის მიხედვით და აფასებენ მართალია მთლიანი გამოსახულება თუ მცდარი ისინი აღინიშნება and და or ით სადაც and მნიშვნელობას უფრო False ანიჭებს და or True 
#5
#  (and)                             (or)
#True and True -- True     |   True or True -- True          # and შემთხვევაში ორივე პასუხი ჭეშმარიტი უნდა იყოს რათა მთლიანი გამოსხაულება ჭეშმარიტი იყოს
#True and False -- False   |   True or False -- True         # or შემტხვევაში ერთი პასუცხი მაინც უნდა იყოს ჭეშმარიტი რათა მთლიანი გამოსახულება ჭეშმარითი იყოს
#False and True -- False     |   False or True -- True
#False and False -- False   |   False or False -- False 
#6
x = True
y = False
x and y 

c = True
b = True 
c and b 
print (x and y )
print (c and b )

x = True
y = False
x or y 

c = False
b = False 
c or b 
print (x or y)
print (c or b)
#7 
building = "house"
age = 15
height = 1.83
honesty = True
print (type(building))
print (type(age))
print (type(height))
print (type(honesty))
#8
building_location = input("Enter building location")
heigt_of_walls = int(input("Enter height of walls"))
price_of_building =float(input("Enter price for building"))
print (building_location)
print (heigt_of_walls)
print (price_of_building)