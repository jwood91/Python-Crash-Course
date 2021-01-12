filename = 'text_files/pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

# when Python reads from a text file, it interprets all text in the file as a
# string.  If you read in a number and want to work with that number in a
# numerical context you will have to convert it to an integer or float using
# the int() or float() functions.

filename = 'text_files/pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string[:52] + "...")
print(len(pi_string))

birthday = input("Enter your birthday in the format ddmmyy: ")
if birthday in pi_string:
    print("Your birthday is in the first million digits of pi!")
else:
    print("Your birthday is not in the first million digits of pi.")
