age = input("What is your age?")
sex = input("What is your gender (m or f) ?")

age = int(age)

if age < 20 and sex == "m":
    print("you are eligible")
else:
    print("you are not eligible")