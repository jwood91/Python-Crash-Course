def count_words(filename):
    """Count the approx number of words in the file"""
    try:
        with open(filename, encoding='utf-8') as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        # Count  the approximate number of words in the file
        words = contents.split()
        num_words = len(words)
        print("This file " + filename + " has about " + str(num_words) +
              " words in it.")


filenames = ['text_files/alice.txt',
             'text_files/siddhartha.txt',
             'text_files/moby_dick.txt',
             ]
for filename in filenames:
    count_words(filename)
