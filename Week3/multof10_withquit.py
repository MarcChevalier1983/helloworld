inp = ""

while True:
    inp = input("Enter a number")

    if inp.upper() == "Q":
        break

    if int(inp) % 10 == 0:
     print("Multiple of 10")
    else:
      print("Not a multiple of 10")
