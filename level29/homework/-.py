# # level 29
# 1)მოცემულია სტრინგი "PythonProgramming".
# ამოიღე პირველი 6 სიმბოლო და დაბეჭდე გამოიყენეთ slicing
str = "PythonProgramming"
print(str[:6])

# 2)მოცემულია სია numbers = [10, 20, 30, 40, 50, 60, 70].
# ამოიღე მხოლოდ შუა 3 ელემენტი და დაბეჭდე გამოიყენეთ slicing (მინუს ინდექსებითაც)
numbers = [10, 20, 30, 40, 50, 60, 70]
print(numbers[2:5])
print(numbers[-5:-2])
# 3)მოცემულია სტრინგი "HelloWorld".
# დაბეჭდეთ Hello ტერმინალში slicing ის გამოყენებით (მინუს ინდექსებითაც)
str_1 = "HelloWorld"
print(str_1[:5])
print(str_1[-10:-5])

# 3)მოცემულია სია letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g'].
# დაბეჭდე ყოველ პირველი მესამე მეხუთე ელემენტები გამოიყენეთ indexing (მინუს ინდექსებითაც)
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[0])
print(letters[2])
print(letters[4])
print(letters[-7])
print(letters[-5])
print(letters[-3])
# 4)მოცემულია სტრინგი "Information".
# ამოიღე "forma" ნაწყვეტი slicing-ით (მინუს ინდექსებითაც)
str_2 = "Information"
print(str_2[2:7])
print(str_2[-9:-4])

# 5)
# მოცემულია სტრინგი "abcdefghijklmno".
# შექმენი სამი სხვადასხვა სლაისი:
str_3 = "abcdefghijklmno"
# პირველი შეიცავდეს მხოლოდ a დან d მდე ასოებს
print(str_3[:4])
print(str_3[-15:-11])
# მეორე – შეიცავდეს j დან o მდე ასოებს
print(str_3[9:])
print(str_3[-6:])
# მესამე – შეიცავდეს f დან j მდე ასოებს
print(str_3[5:10])
print(str_3[-10:-5])