def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def word_count(text):
	words = text.split()
	return f"----------- Word Count ----------\nFound {len(words)} total words"

def char_count(text):
    text = text.lower()
    characters = {}
    for char in text:
    #	characters[char] = characters.get(char, 0) + 1
        if char.isalpha():
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1
    return characters

def sort_on (count):
    return count["count"]

def sorting (characters):
    sorted_list = []
    for char in characters:
        dictionary = { "char": char, "count": characters[char] }
        sorted_list.append(dictionary)	
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def print_sorted_list (sorted_list):
    for item in sorted_list:
        print(f"{item['char']}: {item['count']}")