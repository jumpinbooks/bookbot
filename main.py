
def count_num_words(bookstring):
    wordarray = bookstring.split()
    num_words = 0
    for word in wordarray:
        num_words += 1
    print(f"{num_words} words found in the document")

def get_book_text(path_to_file):
    with open(path_to_file) as f:
    # do something with f (the file) here
    
        # f is a file object
        #file_contents = f.read()
        count_num_words(f.read())

def main():
    get_book_text("./books/frankenstein.txt")
    
main()
