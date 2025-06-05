from stats import count_num_words

def get_book_text(path_to_file):
    with open(path_to_file) as f:
    # do something with f (the file) here
    
        # f is a file object
        #file_contents = f.read()
        count_num_words(f.read())

def main():
    get_book_text("./books/frankenstein.txt")
    
main()
