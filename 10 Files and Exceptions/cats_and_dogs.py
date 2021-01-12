filenames = ["text_files/cats.txt", "text_files/dogs.txt"]

try:
    for filename in filenames:
        with open(filename) as f_obj:
            contents = f_obj.read()
        print(contents)
except FileNotFoundError:
    pass
