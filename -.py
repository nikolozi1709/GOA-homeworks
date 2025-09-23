# #1)შექმენი სია 7 რიცხვით.
numbers = [1,2,3,4,5,6,7]
# დაბეჭდე პირველი და ბოლო ელემენტების ნამრავლი ისე, რომ ორივეჯერ უარყოფითი ინდექსი გამოიყენო.
print(numbers[-1]*numbers[-3])
# დაბეჭდე მესამე ელემენტი მარცხნიდან და მესამე ელემენტი მარჯვნიდან (უარყოფითიინდექსის გამოყენებით).
print(numbers[-5])
print(numbers[-3])
# 2)შექმენი სია "apple", "banana", "cherry", "grape", "kiwi", "orange".
fruits =["apple", "banana", "cherry", "grape", "kiwi", "orange"]
# დაბეჭდე შუა 2 ელემენტი (ორივე(დადებითი და უარყოფითი)) ინდექსით.
print(fruits[-4])
print(fruits[-3])
print(fruits[2])
print(fruits[3])
# 3)
# შექმენი [3,4,5,6,7,1,2,9,8,11]
num =[3,4,5,6,7,1,2,9,8,11]
# მომხმარებელს შემოატანინე ერთი ინდექსი(რიცხვი) 0 დან 10 მდე.
# თუ მომხმარებლის ინდექსი დადებითია → დაბეჭდე ის ელემენტი
index = int(input("enter yur index: "))
if index > 0 and index <=10:
    print(num[index])
else:
    print("you entered negative or more than 10")

# თუ უარყოფით რიცხვი ან  10 ზე მეტი მაღალირიცხვი შემოიყვანა დაბეჭდეთ --> "you entered negative or more than 10  number "


# 4)შექმენით სია ["dog" ," most" ,"is" ,"angry" ,"running"  , "forest", "fast", "in" , "cat" ,"human", "very"]
running_dog = ["dog" ," most" ,"is" ,"angry" ,"running"  , "forest", "fast", "in" , "cat" ,"human", "very"]


# --- მინუს ინდექსების გამოყენებით შეადგინეთ შემდეგი წინადადება და დაბეჭდეთ --> "dog is running in forest very fast"
print(running_dog[-11] + running_dog[-9] + running_dog[-7] + running_dog[-4] + running_dog[-6] + running_dog[-1] + running_dog[-5] )
# --- აასწყვეთ ზემოთ მოცემული წინადადება ოღონდ დადებითი ინდექსებით
print(running_dog[0] + running_dog[2] + running_dog[4] + running_dog[7]+ running_dog[5] + running_dog[-1] + running_dog[6] )
# --- დადებით ინდექსების გამოყენებით ააწყვეთ შემდეგი წინადადება ---> "cat is very angry"
print(running_dog[8] + running_dog[2] + running_dog[-1] + running_dog[3])
# 5)
# შექმენი სია ცხოველებით: ["dog", "cat", "horse", "cow", "sheep", "goat"].
# მომხმარებელს შემოიტანინე ინდექსი(რიცხვი)
animals = ["dog", "cat", "horse", "cow", "sheep", "goat"]
index_1 = int(input("enter any index: "))

if animals[index_1] == "cat":
    print("you choosed cat!")
elif animals[index_1]== "goat":
    print("you choosed goat")
else:
    print("other animal")

# თუ მომხმარებლის მიერ შემოყვანილ ინდექსზე მდგომი ელემენტი არის  "cat", დაბეჭდე "შენ აირჩიე კატა".

# თუ არის "goat", დაბეჭდე "შენ აირჩიე თხა".

# სხვა შემთხვევაში დაბეჭდე "სხვა ცხოველი აირჩიე".
#6)
# შექმენი სია 6 ქალაქით.
# მომხმარებელი შემოიტანს ორ ინდექსს(რიცხვს).
city_names =["Tbilisi","wiatura","qutaisi","gori","zeztafoni","batumi"]
inp_1 = int(input("enter  index1: "))
inp_2 = int(input("enter  index2: "))

if inp_1 < inp_2:
    print(f"{city_names[inp_1]} and {city_names[inp_2]} is chosen")
elif inp_2 < inp_1:
    print(f"{city_names[inp_2]} and {city_names[inp_1]} is chosen")
elif inp_1 == inp_2:
    print(f"{city_names[inp_1]}")
   

# თუ პირველი ინდექსი ნაკლებია მეორეზე → დაბეჭდე ამ ინდექსებზე მდგომი ორივე ელემენტი.

# თუ მეორე ნაკლებია პირველზე → დაბეჭდე "შეცვალე ინდექსები ადგილებით"--->ზემოთ თუ დაპრინტე a და b ამ შემთხვევაში დაპრინტე b და a.

# თუ ინდექსები ერთნაირია → დაბეჭდე "ორივე ერთია" და გამოიტანე ამ ინდექსზე მდგომი ელემენტი ვთქვათ თუ შემოიყვანა მომხმარებელმა 5 და 5 დაუბეჭდე მე 5 ინდექსზე მდგომი ელემენტი.

# 7)მომხმარებელი შემოიტანს სიტყვას.
word = input("enter any word: ")
if word[0] == "a":
    print("first letter is a ! ")
elif word[-1] == "z":
    print("last letter is z ! ")
else:
    print("first letter isnt a and last letter isnt z")

# თუ პირველი ასო "a"-ა → დაბეჭდე "სიტყვა იწყება a-თი".

# თუ ბოლო ასო "z"-ია → დაბეჭდე "სიტყვა მთავრდება z-ით".

# სხვაგვარად → დაბეჭდე "სიტყვა არც a-თი იწყება და არც z-ით მთავრდება".

# 8)დავალება 4

# მომხმარებელი შემოიტანს სიტყვას.
word_0 = input("enter any word: ")
if word[0] == word[-1]:
    print("firts and last letters ar same!")
else:
    print("first and last letters are different!")

# თუ პირველი და ბოლო ასო ერთმანეთს ემთხვევა → დაბეჭდე "პირველი და ბოლო ერთნაირია".

# თუ განსხვავდება → "პირველი და ბოლო განსხვავებულია".


# 9)შექმენი ცვლადი სადაც შეინახავთ შემდეგ ასოებს ---> "agivorsbgitr"
letters =["a","g","i","v","o","r","s","b","g","i","t","r"]

# ----ამ სიიდან შეადგინე სიტყვა "goga, 
print(letters[1]+letters[4]+letters[1]+letters[0])
# ----ამ სიტყვიდან შეადგინე სიტყვა "saba"
print(letters[6]+letters[0]+letters[-5]+letters[0])
# ----ამ სიტყვიდან შეადგინე სიტყვა "bativar"
print(letters[2])

# 10)შექმენი შემდეგი სტრინგი --> 'giorgi'
name_1 = "giorgi"
for i in name_1:
    print(i)
# შენი დავალებააა რომ for დდა while loop ის დახმარებით გამოიტანო ამ სტრინგის თითეული ასო ცალ ცალკე
# 11)გადახედეთ რესურსებს!!!!!!!!!!!!!!!!!!!!!