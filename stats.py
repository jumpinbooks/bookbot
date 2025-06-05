def count_num_words(bookstring):
    wordarray = bookstring.split()
    num_words = 0
    for word in wordarray:
        num_words += 1
    print(f"{num_words} words found in the document")