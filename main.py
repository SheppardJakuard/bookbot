from stats import get_book_text, word_count, char_count, sorting, print_sorted_list
import sys

def main():
	if len(sys.argv) < 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	text = get_book_text(sys.argv[1])
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {sys.argv[1]}")
	print(word_count(text))
	print("--------- Character Count -------")
	print_sorted_list(sorting(char_count(text)))
	sys.exit(0)
	
main()