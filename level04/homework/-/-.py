#1 input - ეს არის ფუნქცია რომელიც საშვალებას გვაძლევს მომხმარებელს შემოვატანინოტ იმფორმაცია კერძოდ terminal ში
# output - შედეგი რომელსაც მნიშვნელობის შეტანის შემდეგ ვიღეთბთ

#2 ცვლადის შექმნა input  ფუნქციის გამოყენებით და type check 
name = input("Enter your name")
print(type(name))

#3 შევქმნათ 5 ცვლადი (str,int,float) თითოეული მონაცემთა ტიპისთვის 

#str -  სტრინგ ტიპის მონაცემები
name_1 = "avto"
name_2 = "dato"
name_3 = "ucha"
name_4 = "gela"
name_5 = "torgva"

# float  ტიპის მონაცემები
height_1 = 1.75
height_2 = 1.77
height_3 = 1.63
height_4 = 1.85
height_5 = 1.70

# int - ინტეჯერ ტიპის მონაცემი 
age_1 = 15
age_2 = 30
age_3 = 40
age_4 = 37
age_5 = 20

#4 3 ცვლადი  (str,int,float) ის გამოყენებით და მონაცემათა ტიპის შემოწმება

# str - string ფუნქციით
name = "nikoloz"
#print(type(name_1))

# int - integer ფუნქციით 
age = 90
#print(type(age))

#float - ტიპისი მონაცემი
height =1.80
print(type(height))

name=input("Enter your name")
surname=input("Enter your surname")
print(name+surname)

score_1 = int(input("Enter your score"))
score_2 = int(input("Enter your score"))
score_3 = int(input("Enter your score"))
score_4 = int(input("Enter your score"))
score_5 = int(input("Enter your score"))
print(((score_1+score_2+score_3+score_4+score_5 )/5))

name = input("Enter your name")
surname = input("Enter your surname")
age = input("Enter your age")
height = input("Enter your height")
weight = input ("Enter your weught")
print(name+surname+age+height+weight)