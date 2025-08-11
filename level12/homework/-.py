# 1)
#კომენტარების სახით თავიდან ახსენით რა არის conditional statement, რა დანიშუნლება გააჩნიათ და როგორი სახის განცხადებები გვაქვს.

#conditional statement - ეს არის (პირობითი განაცხადი) და გვაქვს if და else განაცხადი 
#სადაც if არის იგივე თუ ანუ რაღაც პირობა და  რაც შეეხება else თუ პირობა არ შესრულდება შემდგომ მოსახდენი ოპერაციის შემცველია იგი 

# 2) for ციკლის მეშვეობით გამოიტანეთ "hello world" 50-ჯერ.
for i in range(50):
    print(str(i) + "hello world")

#3) while ციკლის მეშვეობით გამოიტანეთ რიცხვები 3-დან 17-ის ჩათვლით.
i = 3
i +=1
while i <= 17:
    print(i)
    i +=1
#4) მომხმარებელს შემოატანინეთ პაროლი, შემდეგ კი შედეგი შეინახეთ ცვლადში. შექმენით პირობა თუ ის უდრის "1234"-ს დაბეჭდეთ "Password is correct", სხვა შემთხვევაში დაბეჭდეთ "Password is incorrect"
password = 1234
input("Enter your password")
if password ==input:
    print("Password is incorect!")
else:
    print("Password is correct!")
#5)შექმენით ცვლადი სადაც შეინახავთ მომხმარებლის მიერ შემოყვანილი ცხოველის სახეობას. თუ სახეობა უდრის "ძაღლი" დაბეჭდეთ "woaf! woaf!", სხვა შემთხვევაში "შენ არ გყავს ძაღლი"
animal_type ="dog"
input("Enter your animal Type")
if animal_type == input:
    print("woaf")
else:
    print("you dont have dog")
#)6 უყურეთ შემდეგ ვიდეო წყაროსს:

#-- https://youtu.be/FvMPfrgGeKs --
