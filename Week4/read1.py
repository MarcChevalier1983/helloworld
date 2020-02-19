with open('my_input_file.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())