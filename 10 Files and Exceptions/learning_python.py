filename = "text_files/learning_python.txt"

with open(filename) as file_object:
    contents = file_object.read()
    print(contents.rstrip())


with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())


with open(filename) as file_object:
    contents = file_object.readlines()

for line in contents:
    print(line.rstrip())


with open(filename) as file_object:
    contents = file_object.readlines()

for line in contents:
    line = line.rstrip()
    print(line.replace('Python', 'C'))
