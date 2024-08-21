# word_count_aggregator should return a function that calculates
# the number of words in its input (doc, a string). It should
# then add that number to an *enclosed* count value and return
# the new count. In other words, it keeps a running total of the
# count variable within a closure.
#
# Tip: use .split() to count the number of words in the `doc` string.


def word_count_aggregator():
    count = 0

    def word_counter(doc):
        nonlocal count
        count += len(doc.split())
        return count

    return word_counter


test_cases = [
    (
        [
            "Welcome to the jungle",
            "We've got fun and games",
            "We've got everything you want honey",
        ],
        15,
    )
]


def test(inputs, expected_output):
    print("--------------------------------")
    print(f"Input:")
    for x in inputs:
        print(f" * {x}")
    print(f"Expecting: {expected_output}")
    aggregator = word_count_aggregator()

    try:
        for input in inputs:
            result = aggregator(input)
    except Exception as e:
        result = e
    print(f"Actual: {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("=============== PASS ================")
    else:
        print("=============== FAIL ================")
    print(f"{passed} passed, {failed} failed")


main()
