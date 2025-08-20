from stats import get_book_text, get_num_letters


def main():
    text = get_book_text("./books/frankenstein.txt")
    length = get_num_letters(text)
    print(length)


main()
