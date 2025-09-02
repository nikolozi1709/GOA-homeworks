# 1)მომხმარებელს შემოატანინეთ ორი რიცხვი,შეამოწმეთ თუ პირველი რიცხვი მეტია მეორე რიცხვზე დაპრინტე რომ ‘first is more than second’,ასევე შეამოწმე თუ პირველი რიცხვი ნაკლებია მეორე რიცხვზე დაპრინტე რომ ‘first is less than second’ და სხვა დანარჩენ შემთხვევაში დაპტინტე რომ ‘first number equal to second number’
num_1 = int(input("enter any number"))
num_2 = int(input("enter any number"))
if num_1 > num_2:
    print("num_1  is more than num_2!")
elif num_1 < num_2:
    print("first number is less than second!")
else:
    print("firs and second number are equal!")
#2)მომხმარებელს შემოატანინე რაიმე სტრინგი,ასევე შექმენი ცვლადი სადაც შეინახავთ თქვენს სახელს,შემდეგ შეამოწმე თუ მომხმარებლის შემოყვანილი სტრინგი უდრის შენა სახელს დაუპრინტე რომ ‘სეხნიები ვართ’ სხვა შემთხვევაში დაუპრინტეთ რომ ‘სხვადასხვა სახელები გავქვს’
name_1 = "vaxtangi"
name_2 = input("enter a name: ")
if name_1 == name_2:
    print("we have same names!")
else:
    print("our name are different!")
#3)შექმენი ორი ცვლადი სადაც შეინახავთ ინტეჯერ ტიპოს მონაცემებს,თქვენი დავალებაა შეამოწმოთ,თუ პირველი რიცხვი მეტია 0 ზე და და მეორე რიცხვიც მეტია 0 ზე დაუპრინტე რომ ‘ორივე რიცხვი დადებითია, ასევე შეამოწმე თუ პირველი რიცხვი ნაკლებია 0 ზე და მეორე რიცხვიც ნაკლებია 0 ზე დაპურინტე რომ  ‘ორივე რიცხვი არის უარყოფით’,სხვა დანარჩენ შემთხვევაში დაუპრინტე რომ ‘ეს რა ჯანდაბაა’
num1 = int(input("enter any number: "))
num2 = int(input("enter any number: "))
if num1 > 0  and num2 >0:
    print("both of the numbers are positive!")
elif num1 > 0 and num2 < 0:
    print("one of the number is negative!")
elif num1 < 0 and num2 >0:
    print("one of the number is negative!")
elif num1 <0 and num2 < 0:
    print("both numbers are negative!")
else:
    print("what is this!")
#4)დაატრიალეთ ფორ ლუპი 50 დან 100 მდე 2 ის გამოტივებით 
for i in range(50,100,2):
    print(i)
#5)ვაილ ლუპის გამოყენებით 20 დან 40 მდე გამოიტანეთ ყველა რიცხვი
num = 20 
while num < 40:
    num += 1
    print(num)
# 6)სოლოლერნი შეასრულეთ Modil 4 quiz ის ჩათვლით