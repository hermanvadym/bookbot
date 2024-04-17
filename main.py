def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words were found in the document\n\n")
    char_dict = get_char_number(text)
    #print(char_dict)
    char_list = get_sort_on(char_dict)
    for d in char_list:
        print(f"The '{d["letter"]}' character was found {d["amount"]} time")
    print("--- End report ---")

def get_char_number(text):
    chars = {}    
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_num_words(text):
    words = text.split()
    return len(words)


def sort_on(char_list):
    return char_list["amount"]


def get_sort_on(char_dict):
    char_list = []
    for key in char_dict:
        if key.isalpha():            
            char_list.append({"letter": key, "amount": char_dict[key]})
    char_list.sort(reverse=True, key=sort_on)
    return char_list


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()