import sys
from stats import word_count
from stats import char_count
from stats import sort_char_count


def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()

    return contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    contents = get_book_text(filepath)
    num_words = word_count(contents)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    sorted_char_counts = sort_char_count(char_count(contents))
    print("--------- Character Count -------")
    for item in sorted_char_counts:
        if item["char"].isalpha():
            print(item["char"] + ": " + str(item["num"]))
    print("============= END ===============")

main()
