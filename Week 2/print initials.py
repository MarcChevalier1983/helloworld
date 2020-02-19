first_name = input("What is your first name?")
last_name = input("What is your last name?")

first_name = first_name.strip().upper()
last_name = last_name.strip().upper()

# print("The initials are %s and %s" % (first_name[0], last_name[0]))

print("The initials are {0} and {1}".format(first_name[0], last_name[0]))

