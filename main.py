import sys
from stats import get_num_words, get_num_chars, get_sorted


def main():
	book_path = get_book()
	text = get_book_text(book_path)
	num_words = get_num_words(text)
	char_count = get_num_chars(text)
	sorted_list = get_sorted(char_count)
	print_report(book_path, num_words, sorted_list)



def get_book_text(path):
	with open(path) as f:
		return f.read()



def print_report(book_path, num_words, sorted_list):
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {book_path}...")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")
	for dict in sorted_list:
		print(f"{dict['char']}: {dict['num']}") 
	print("============= END ===============")


def get_book():
	if len(sys.argv) !=2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	else:
		return sys.argv[1]

main()

