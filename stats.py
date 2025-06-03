def word_count(file_contents):
    words = file_contents.split()
    counter = 0

    for word in words:
        counter += 1

    return counter

def count_characters(book_text):
    small_characters = book_text.lower()
    single_characters = {}

    for character in small_characters:
        if character in single_characters:
            single_characters[character] += 1
        else:
            single_characters[character] = 1
    return single_characters

def sort_on(dict):
    return dict["amount"]

def naming_keys(character_count):
    sorted_list = []
    for character in character_count:
        amount = character_count[character]
        sorted_list.append({"character": character,"amount": amount})
    
    new_list = []
    sorted_list.sort(reverse=True, key=sort_on)
    for key in sorted_list:
        if key["character"].isalpha() == True:
            new_list.append(key["character"]+": "+str(key["amount"]))
        else:
            continue

    return new_list

    


    