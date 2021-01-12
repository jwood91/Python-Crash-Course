filename = 'text_files/alice.txt'

try:
    with open(filename, encoding='utf-8') as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = ("Sorry this file " + filename + " does not exist")
    print(msg)
else:
    # Count  the approximate number of words in the file
    words = contents.split()
    num_words = len(words)
    print("Alice in Wonderland has about " + str(num_words) + " words in it.")
