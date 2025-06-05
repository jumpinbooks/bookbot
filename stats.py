def count_num_words(bookstring):
    wordarray = bookstring.split()
    num_words = 0
    for word in wordarray:
        num_words += 1
    print(f"{num_words} words found in the document")
    
def count_each_letter(bookstring):
    lowstring = bookstring.lower()
    bookdict = {}
    for onechar in lowstring:
        count = bookdict.get(onechar, 0)
        if count == 0:
            bookdict[onechar] = 1
        else:
            bookdict[onechar] = count + 1
    for onechar in bookdict:
        print(f"'{onechar}':", bookdict[onechar])
    return bookdict