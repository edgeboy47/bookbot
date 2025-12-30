def get_book_words(book: str):
    return len(book.split())


def count_chars(book: str):
    chars = {}
    for char in list(book):
        if not char or not char.isalpha():
            continue

        char = char.lower()
        if char in chars:
            chars[char] = chars[char] + 1
        else:
            chars[char] = 1

    return chars


def sort_chars(chars: dict[str, int]):
    def sorter(items):
        return items["num"]

    chars_list = []
    for char in chars:
        chars_list.append({"char": char, "num": chars[char]})

    chars_list.sort(reverse=True, key=sorter)
    return chars_list
