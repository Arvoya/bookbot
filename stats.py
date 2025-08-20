
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def get_num_letters(text):
    counts = {}
    for letter in text:
        if letter.lower() in counts:
            counts[letter.lower()] += 1
        else:
            counts[letter.lower()] = 1
    return counts
