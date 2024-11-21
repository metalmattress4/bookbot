def count_words(words_to_count):
    
    individual_words = words_to_count.split()
    
    return len(individual_words)

def count_characters(book_contents):
    
    book_contents = book_contents.lower()
    character_counts = {}

    for character in book_contents:
        if not character.isalpha():
            continue
        elif character not in character_counts:
            character_counts[character] = 1
        else:
            character_counts[character] += 1
    
    return character_counts

def print_character_counts_nicely(character_counts):

    counts_list = []

    for entry in character_counts:
        entry_to_add = {"name": entry, "num": character_counts[entry]}
        counts_list.append(entry_to_add)
    
    counts_list.sort(reverse=True, key=sorting_key)
    
    for entry in counts_list:
        print(f"The '{entry["name"]}' character was found '{entry["num"]}' times.")

def sorting_key(dict):
    return dict["num"]

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    print(file_contents)

    num_words = count_words(file_contents)
    character_counts = count_characters(file_contents)

    print(f"There are {num_words} words in this book.")
    print_character_counts_nicely(character_counts)

main()
