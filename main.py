from stats import get_book_text, word_count, char_count, sorting, print_sorted_list

def main():
	text = get_book_text("books/frankenstein.txt")
	print("============ BOOKBOT ============")
	print("Analyzing book found at books/frankenstein.txt")
	print(word_count(text))
	print("--------- Character Count -------")
	print_sorted_list(sorting(char_count(text)))
	
main()