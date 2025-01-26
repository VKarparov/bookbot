from collections import Counter

path_to_file = "books/frankenstein.txt"

def letters_count(content):
    return Counter(content.lower())

def words_count(content):
    return len(content.split())

def main():
    with open(path_to_file) as f:
        file_contents = f.read()
    
    letter_dict = letters_count(file_contents)
    # Display general data
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{words_count(file_contents)} words found in the document")
    print("\n")

    # Display report for each letter in list
    for letter in letter_dict:
        if letter.isalpha():
            print(rf"The '{letter}' character was found {letter_dict[letter]} times")
    
    print("--- End report ---")

main()