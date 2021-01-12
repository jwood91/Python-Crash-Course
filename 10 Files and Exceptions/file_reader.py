# if you have a long filepath store this in a variable and then pass it
# into the open()
filename = 'text_files/pi_digits.txt'

with open(filename) as file_object:
    contents = file_object.read()
    print(contents.rstrip())

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# readlines() takes each line of the file and stores it in a list. this lets
# you have access outside of the with block as after each with block the
# file is closed so you can store the information in a list for use outside
# of the block as below:
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))
