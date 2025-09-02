num_1 = int(input("Enter any number "))
num_2 = int(input("Enter any number "))
num_3 = int(input("Enter any number "))
if num_1 == num_2:
    print("num_1 and num_2 are equal")
elif num_2 == num_3:
    print("num_2 and num_3 are equal")
elif num_3 == num_1:
    print("num_3 and num_1 are equal")
else:
    print("there was no imputs with same value")

month = int(input("enter any number from 1-12: "))
if month in (12,1,2):
    print("ზამთარი")
elif month in (3,4,5):
    print("გაზაფხული")
elif month in (6,7,8):
    print("ზაფხული")
elif month in (9,10,11):
    print("შემოდგომა")
else:
    print("არასწრორი")

# #3) შემოატანინეთ მომხმარებელს თავისი სახელი:
# თუ სახელი უდრის admin:
#    მოთხოვეთ შემოიყვანოს ადმინის პაროლი:
#       თუ პაროლი უდრის adminpassword123:
#         დაპრინტეთ სალამი ადმინ
#       სხვა შემთხვევაში:
#         დაპრინტეთ წვდომა არ გაქვს
# სხვა შემთხვევაში:
#   დაპრინტეთ სალამი მომხმარებელო

name_1 = input("enter your name here ")
if name_1 == "admin":
    password = input("enter your password here: ")
    if password == "adminpassword123":
        print("hello admin!")
    else:
        ("there was no correct operation!")
