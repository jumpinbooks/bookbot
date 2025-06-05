def count_num_words(bookstring):
    wordarray = bookstring.split()
    num_words = 0
    for word in wordarray:
        num_words += 1
    return num_words
    
def count_each_letter(bookstring):
    lowstring = bookstring.lower()
    bookdict = {}
    for onechar in lowstring:
        count = bookdict.get(onechar, 0)
        if count == 0:
            bookdict[onechar] = 1
        else:
            bookdict[onechar] = count + 1
#    for onechar in bookdict:
#        print(f"'{onechar}':", bookdict[onechar])
    return bookdict

def dict_to_sorted_list(bookdict):
    list_of_values = []
    for key, value in bookdict.items():
        list_of_values.append(value)
    list_of_values.sort(reverse = True)
    
    list_of_dict = []
    for target_value in list_of_values:

        for key, value in bookdict.items():
            if value == target_value:
                temp_dict = {
                    "char": key,
                    "num": value
                }
                list_of_dict.append(temp_dict)
                
    return list_of_dict