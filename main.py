import sys
from stats import count_chars, get_book_words, sort_chars


def get_book_text(filepath: str):
    out = ""
    with open(filepath) as file:
        data = file.read()
        out = data
    return out


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = get_book_words(book_text)
    chars = count_chars(book_text)
    sorted_chars = sort_chars(chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in sorted_chars:
        print(f"{char['char']}: {char['num']}")
    print("============= END ===============")


if __name__ == "__main__":
    main()
