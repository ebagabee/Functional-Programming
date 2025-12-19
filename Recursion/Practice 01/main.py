def find_longest_word(document, longest_word=""):
    if len(document) == 0:
        return longest_word

    parts = document.split(maxsplit=1)

    if len(parts) == 0:
        return longest_word

    first_word = parts[0]

    if len(first_word) > len(longest_word):
        longest_word = first_word

    if len(parts) == 1:
        return longest_word

    rest = parts[1]

    return find_longest_word(rest, longest_word)
