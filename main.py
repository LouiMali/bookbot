def get_book_text(path_to_file):
    file_contents = ""
    
    with open(path_to_file) as f:
        file_contents = f.read()


    return file_contents

def word_count(file_contents):
    words = file_contents.split()
    counter = 0

    for word in words:
        counter += 1

    return counter


def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = word_count(book_text)
    print(f"{num_words} words found in the document")

main()