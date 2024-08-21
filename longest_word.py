# Complete the find_longest_word function without a loop.
# It accepts a string input, document, and a string input, longest_word,
# that is the current longest word and which defaults to an empty string
# - Check if the first word is longer than the current longest_word,
# then recur for the rest of the document.
# - Ensure there are no potential index errors.


def find_longest_word(document, longest_word=""):
    words = document.split()
    if not words:
        return longest_word
    test_word = words[0]
    if len(test_word) > len(longest_word):
        longest_word = test_word
    return find_longest_word(" ".join(words[1:]), longest_word)


run_cases = [
    ("Either that wallpaper goes, or I do.", "wallpaper"),
    (
        "Then I die happy",
        "happy",
    ),
    (
        "Et tu, Brute?",
        "Brute?",
    ),
]


def main():
    for case in run_cases:
        result = find_longest_word(case[0])
        expected = case[1]
        print(f"Result: {result}, Expected: {expected}, Pass: {result == expected}")


if __name__ == "__main__":
    main()
