#1)შექმენით ცვლადი სადაც შეინახავთ ინტეჯერ ტიპის მონაცემს,შემდეგ შეამოწმეთ თუ ეს რიცხვი რომელიც ცვლადში გაქვთ შენახული მეტია 10 ზე დაპრინტეთ "more than 10" სხვა შემთხვებაში დაპრინტეთ "less than 10"
variable_0 = 10
if variable_0 > 10:
    print("more than 10")
elif variable_0 <10:
    print("less than 10")
else:
    print("equal to 10")

#2)მომხმარებელს შემოაყვანინეთ რიცხვი,შემდეგ შეამოწმეთ თუ ეს რიცხვი უდრის 15 ს დაუპრინტეთ "equal to 15" სხვა შემთხვევაში დაუპრინტეთ "not equal to 15"
num_1 = int(input("Enter any Number"))
if num_1 == 15:
    print("equal to 15")
else:
    print("not equal to 15")
#3)მომხმარებელს შემოატანეთ სტრინგი შენი დავალებაა შეამოწმო,თუ მომხამრებლის მიერ შემოყვანილი სტრინგი არის giorgi დაუპრინტეთ 'you are correct" სხვა შემთხვევაში დაუპრინტეთ "you are wrong"
name_1 = str(input("Enter your name "))
if name_1 == "giorgi":
    print("your name is correct! ")
else:
    print("youjr name is wrong ! ")
#4)დაატრიალეთ ფორ ციკლი 50 დან 100 მდე 5 ის გამოტოვებით
for i in range(50,100,5):
    print (i)
#5)ფორ ციკლის დახმარებით გამოიტანეთ ტერმინალში თქვენი სახელი და გვარი
for i in range(0,10):
    print(str(i)+"ნიკოლოზ ქუსიკაშვილი")
#6)while loop ის დახმარებით ტერმინალში გამოიტანეთ რიცხვები 20 დან 50 მდე
num_2 = 20 
while num_2 <50:
    num_2 += 1
    print(num_2)