from stats import count_each_letter

def get_book_text(path_to_file):
    with open(path_to_file) as f:
    # do something with f (the file) here
    
        # f is a file object
        #file_contents = f.read()
        #count_num_words(f.read())
        count_each_letter(f.read())

def main():
    get_book_text("./books/frankenstein.txt")
    
main()
