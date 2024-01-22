def main():
    path_to_file="books/frankenstein.txt"
    text = read_book_text(path_to_file)
    num_words = count_words(text)
    char_dict = count_letters(text)
    report(path_to_file, char_dict, num_words)

def read_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_char(report_list):
    return sum(entry[1] for entry in report_list)

def count_letters(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def report(path_to_file, char_dict, word_count):
    report_list = [(key, value) for key, value in char_dict.items() if key.isalpha()]
    report_list.sort()
    character_count = count_char(report_list)

    print(f'--- Begin report of {path_to_file} ---')
    print(f'{word_count} words found in the document')
    print(f'{character_count} characters found in the document\n')

    for entry in report_list:
        print(f'The {entry[0]} character was found {entry[1]} times')

    print(f'-- End Report ---')
    


main()