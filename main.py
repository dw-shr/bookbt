from operator import itemgetter

path_to_file = './books/frankenstein.txt'

def open_book(book_path):
    with open(book_path) as f:
        f = f.read()
        return f

def get_wordcount(book):
    return len(book.split(" "))

def get_letter_appearance(book):
    letter_dict = {}
    for word in book:
        for letter in word:
            if letter.isalpha():
                letter = letter.lower()
                if letter in letter_dict:
                    letter_dict[letter] += 1
                else:
                    letter_dict[letter] = 1
    return letter_dict

def sort_dict_by_value(dictionary):
    new_list = []
    for k, v in dictionary.items():
        new_list.append({"letter": k, "count": v})
    sorted_list = sorted(new_list, key=itemgetter("letter"), reverse=False)
    return sorted_list



def main():
    book = open_book(path_to_file)
    wordcount = get_wordcount(book)
    print(f"Word count: {wordcount}")
    letter_appearance = get_letter_appearance(book)
    print(f"Letter appearance: {letter_appearance}")

    for dict in sort_dict_by_value(letter_appearance):
        print(f"Letter: {dict['letter']} \nCount: {dict['count']}\n===")



main()