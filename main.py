from stats import count_num_words
from stats import count_each_letter
from stats import dict_to_sorted_list

def process_book(path_to_file):

    with open(path_to_file) as f:
    # do something with f (the file) here
        num_words = count_num_words(f.read())
        f.seek(0) # Reset the file pointer to the beginning
        sorted_dict = dict_to_sorted_list(count_each_letter(f.read()))

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path_to_file}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        
        for dictionary in sorted_dict:
            if dictionary["char"].isalpha():
                print(f"{dictionary['char']}: {dictionary['num']}")
                    
        print("============= END ===============")

def main():
    process_book("./books/frankenstein.txt")
    
main()
