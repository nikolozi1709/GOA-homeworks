# 1)მოცემულია სია --> [1, 2, 3, 4, 5, 6]
# შეცვალე შუა ორი ელემენტი რიცხვებით [10, 20, 30].
num_0 = [1, 2, 3, 4, 5, 6]
num_0[2:4] = [10,20,30]
print(num_0)

# 2)მოცემულია სია --> ["apple", "banana", "cherry", "kiwi", "mango"]
# შეცვალე პირველი ორი ელემენტი სიით ["pear", "plum"].
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruits[0:2] = ["pear", "plum"]
print(fruits)
# 3)ოცემულია სია --> ["a", "b", "c", "d", "e", "f"]
# შეცვალე ბოლო სამი ელემენტი სიით ["x", "y", "z"].
list = ["a", "b", "c", "d", "e", "f"]
list[3:] = ["x", "y", "z"]
print(list)
# 4)მოცემულია სია --> ["red", "green", "blue", "yellow", "black", "white"]
# შეცვალე ინდექსებზე 2-დან 5-მდე ელემენტები სიით ["purple", "orange"].
colors = ["red", "green", "blue", "yellow", "black", "white"]
colors[2:] = ["purple", "orange"]
print(colors)
# 5)მოცემულია სია --> ["გიორგი" , "ირმა" , "საბა" ]
# შეცვალე მთლიანი სია შემდეგი სიით -->  ["red", "green", "blue", "yellow", "black", "white"]
names = ["გიორგი" , "ირმა" , "საბა" ]
names = ["red", "green", "blue", "yellow", "black", "white"]
print(names)
# ===========================================

# 6) მომხმარებელმა შეიყვანოს რიცხვი — შეამოწმე ლუწია თუ კენტი ეს რიცხვი , თუ ლუწია დაპრინტე --> "Even" ,თუ კენტია დაპრინტე --> "Odd".
number = int(input("enter any number! "))
if number % 2 ==0:
    print("this number is even !")
elif number % 2 !=0:
    print("your number is odd!")
# 7)შექმენი სია --> სადაც შეინახავ ინტეჯერებს ,შემდეგ შეამოწმე თუ სიაში მყოფი მე3 ინდექსზე მდგომი ელემენტი არუს ლუწი დაპრინტე --> "Even number" ,თუ სიაში მყოფი მესამე ინდექსზე მდგომი ელემენტი არის კენტი დაპრინტე --> "Odd number"
nums = [1,2,3,4,5,6,7]
if  nums[1] % 2 ==0:
    print("number is even!")
else:
    print("numbers is odd! ")

# 8)შექმენი სია სადაც შეინახავ ინტეჯერებს, თუ სიაში მყოფი ბოლო ელემენტი არის ლუწი და მეტი 50 ზე დაპრინტე --> "ეს რიცხვი არის ლუწი და მეტი 50 ზე" , თუ რიცხვი არის კენტი და ნაკლებია 50 ზე დაპრინტე --> "ეს რიცხვი არის კენტი და ნაკლები 50 ზე"
numbers = [10,20,30,40,50]
if numbers[4] % 2 ==0 and numbers[4] >= 50:
    print("this number is even and more  or equal to  50!")
else:
    print("this number is odd and less than 50!")


# 9)შექმენი სია სადაც შეინახავ ინტეჯერებს,თუ სიაში მყოფი მე 5 ინდექსზე მდგომი ელემენტი არის ლუწი ან 100 ზე მეტი დაუპრინტე --> "even or more than 100" ,თუ სიაში მყოფი მესამე ინდექსზე მდგომი ელემენტი არის კენტი ან ნაკლები 100 ზე დაუპრინტე --> odd or less than 100
numbers_1 = [50,70,90,110,130,150,170]
if numbers_1[5] % 2 ==0 or numbers_1[5] > 100:
    print("even or more than 100")
elif numbers[3] % 2 !=0 or numbers[3] < 100:
    print("odd or less than 100")
else:
    print("get out!")


# ==============================================================

# 10)შექმენი ორი ცვლადი სადაც შეინახავთ სტრინგებს , შემდეგ შეადარე უდრის თუ არა ეს ორი ცვლადი ერთმანეთს , გამოიყენე ახლად ნასწავლი ოპერატორი != 
age_of_vaxo = 20
age_of_shota = 25
if age_of_vaxo == age_of_shota:
    print("you guys are the same age!")
elif age_of_shota != age_of_vaxo:
    print("get out! ")