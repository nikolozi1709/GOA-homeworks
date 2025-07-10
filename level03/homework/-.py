# 1 ცვლადი მათემატიკური ოპერაციებით
num_1 = 100
num_2 = 10
sum_of_numbers = num_1 + num_2
print(sum_of_numbers)
sum_of_numbers = num_1 - num_2
print(sum_of_numbers)
sum_of_numbers = num_1 * num_2
print(sum_of_numbers)
sum_of_numbers = num_1 / num_2
print(sum_of_numbers)

#2ცვლადი სახელად name
name="avtandila"
print(name)
name="davita"
print(name)
name="lashvarda"
print(name)
name="lukito"
print(name)
name="nikoloza"
print(name)

#3case sensitive ცვლადები
LoCation="gldani"
locaTioN="isani"
locatioN="digomi"
loCation="marjanishvili"
LOcaTioN="vake"
print(LoCation)
print(locaTioN)
print(locatioN)
print(loCation)
print(LOcaTioN)

#4 შეცდომების გასწორება   
     # შესწორებული                    # არასწორი                               ახსნა განმარტება
name2 = "giorgi"        # 2name = "giorgi"           name2 ან name_2 ციფრის ცვლადის სახელის წინ დაწერა არ შეიძლება
username = "bubunauri"  #user{name = "bubunauri    user_name ან username არ საჭიროებს ფიგურულ ფრჩხილს
user_name = "goga"        # user_name = goga           string იწერება "" ბრჭყალებში
user_surname = "axalaia"   #user-surname = axalaia     აქ underscore არის საჭირო და string იწერება "" ბრჭყალებში

# 5 snake_case ის გამოყენებით 5 ცვლადის შექმნა string ებს შორის ანუ კონკატინაცია
name_1="avtandila "
name_2="temura "
name_3="vaxo "
name_4="jambula "
name_5="chitovichi"
print(name_1+name_2+name_3+name_4+name_5)

#6 ამოცანა 2 ცვლადის მათემატიკური ოპერაციის გამოყენებით
name = "nikolozi"
age = 10
print(name*age)

#7 რომელი მათემატიკური მოქმედება არ სრულდება string ზე და integer ზე და რა არის შედეგი?
# string სა და ინტეჯერს შორის არ შეიძლება არანაირი მათემატიკური ოპერაცია გარდა * გამრავლებისა წინააღმდეგ შემთხვევაში terminal ში TypeError ს მივიღებთ