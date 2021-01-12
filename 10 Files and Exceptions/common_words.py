filename = "text_files/moby_dick.txt"

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
        whale = contents.lower().count('whale')
        print("whale is said approximately " + str(whale) + " times in "
              + filename)
except FileNotFoundError:
    print("This file does not exist!")
