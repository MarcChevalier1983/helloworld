# first_list = list(range(1,6))
#
# second_list = first_list
#
# print(first_list)
# print(second_list)
#
# second_list[2] = 99
#
# print(first_list)
# print(second_list)

# WHAT THIS DOES IS MAKE BOTH LISTS THE SAME, EVEN IF YOU CHANGE THE 2ND AFTERWARDS
# TRY BELOW FOR 2 SEPARATE LISTS

first_list = list(range(1,6))

second_list = first_list.copy()

print(first_list)
print(second_list)

second_list[2] = 99

print(first_list)
print(second_list)