filename = "text_files/programing.txt"

# 'w' is write mode == 'r' is read mode == 'a' is append mode.
with open(filename, 'w') as file_object:
    file_object.write("I love programming\n")
    file_object.write("I really love programming\n")

with open(filename, 'a') as file_object:
    file_object.write("oi oi!\n")
    file_object.write("MORNING!\n")
