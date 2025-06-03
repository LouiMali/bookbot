
from stats import word_count
from stats import count_characters
from stats import naming_keys

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = word_count(book_text)
    character_count = count_characters(book_text)
    sorted_list = naming_keys(character_count)
    
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for list in sorted_list:
        print(list)
    print("============= END ===============")



def get_book_text(path_to_file):
    file_contents = ""
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents



main()