number_guests = input("How many guests are expected?")

if int(number_guests) <= 8:
    print("A table is available")
else:
    print("No tables available")
