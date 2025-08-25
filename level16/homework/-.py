#1) მომხმარებელს შემოაყვანიეთ რაიმე რიცხვი(მთელი/ათწილადი); შეამოწმეთ ეს რიცხვი - 
#--> თუ დადებითია დაპრინტეთ 'ეს რიცხვი დადებითი რიცხვია'
#--> თუ უარყოფითია დაპრინტეთ 'ეს რიცხვი უარყოფითი რიცხვია'
#--> თუ ნულია დაპრინტეთ 'ეს რიცხვი ნულია'
num_0 = int(input("Enter any number "))
if num_0 > 0:
    print("your number is positive!")
elif num_0 < 0:
    print("your number is negative!")
else: 
    print("you number is equal to 0")

#2) მომხმარებელს შემოაყვანიეთ თავისი ასაკი:
#0–12 წლის ასაკი --> დაპრინტეთ 'ბავშვი ხარ'
#13-19 წლის ასაკი --> დაპრინტეთ 'მოზარდი/თინეიჯერი ხარ'
#20-64 წლის ასაკი --> დაპრინტეთ 'ზრდასრული ხართ'
#65-120 წლის ასაკი --> დაპრინტეთ 'ხანში შესული ხართ'
#120 და ზემოთ --> დაპრინტეთ 'გურუ ან ჯადოქარი'
#თუ შემოყვანილი ასაკი უარყოფითია --> დაპრინტეთ 'არასწორი ინფო'
age_0 = int(input("enter your age here "))
if age_0 < 13:
    print("you are still a kid")
elif age_0 > 12 and age_0< 20:
    print("you are teen")
elif age_0 > 19 and age_0 < 65:
    print("you are adult")
elif age_0 > 65 and age_0 < 121:
    print("getting old")
else :
    print("you are lying or dead")

# 3) დაწერეთ "password guesser" პროგრამა, შექმენით რაიმე ცვლადი და მასში შეინახეთ ის პაროლი რომელსაც ყველგან იყენებთ ;)
#მომხმარებელს მოთხოვეთ გამოიცნოს თქვენი პაროლი
#აღნიშნეთ ცდების რაოდენობა
#გამოიყენეთ while loop, მანამ ატრიალეთ სანამ მომხმარებელი პაროლს არ გამოიცნობს ან დაწერს --> 'nah strong password'
#ბოლოს აჩვენეთ(დაუპრინტეთ) რამდენი ცდა დაჭირდა პაროლის გამოსაცნობად
password = "kitri"
attempts = 0 
work = True
while work:
    user_inp = input("Enter a password ") 
    if user_inp == password:
        attempts +=1 
        print(f"your password is correct! attempts: {attempts}")
        break
    else:
        attempts += 1 
        print(f"incorrect password attempts already used {attempts}")
#4) მომხმარებელს შემოატანიეთ სამი რიცხვი(მთელი/ათწილადი) და ამ სამი რიცხვთაგან დაბეჭდეთ უდიდესი
num_1 = int(input("Enter any number "))
num_2 = int(input("Enter any number "))
num_3 = int(input("Enter any number "))
if num_1 > num_2 and num_1 > num_3:
    print(f"num_1 is the biggest number {num_1}")
elif num_2 > num_1 and num_2 > num_3:
    print(f"num_2 is the biggest nuimber {num_2}")
else:
    print(f"num_3 is the biggest {num_3}")

#5) შემოატანიეთ მომხმარებელს რიცხვი 1-დან 7-ჩათვლით
# თუ 1 --> დაპრინტეთ 'ორშაბათი'
# თუ 2 --> დაპრინტეთ 'სამშაბათი'
# თუ 3 --> დაპრინტეთ 'ოთხშაბათი'
# თუ 4 --> დაპრინტეთ 'ხუთშაბათი'
# თუ 5 --> დაპრინტეთ 'პარასკევი' 
# თუ 6 --> დაპრინტეთ 'შაბათი'
# თუ 7 --> დაპრინტეთ 'კვირა' 
# სხვა დანარჩენი --> 'არ ვიცი ეგ რა დღეა'
choice = input("choose any operation 1/2/3/4/5/6/7")
if choice == "1":
    print("ორშაბათი")
elif choice == "2":
    print("სამშაბათი")
elif choice == "3":
    print("ოთხშაბათი")
elif choice == "4":
    print("ხუთშაბათი")
elif choice == "5":
    print("პარასკევი")
elif choice == "6":
    print("შაბათი")
elif choice == "7":
    print("კვირა")
else:
    ("არასწორი ოპერაცია")