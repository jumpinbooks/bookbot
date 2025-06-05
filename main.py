import sys
from stats import count_num_words
from stats import count_each_letter
from stats import dict_to_sorted_list

args = sys.argv

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
    if len(args) == 2:
        process_book(args[1])
    else:    
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

#    print(len(args))
main()
