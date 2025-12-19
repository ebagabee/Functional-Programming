# Recursion Practice

In Doc2Doc, we have a search function to find the longest word in a document.

## Assignment

Complete the `find_longest_word` function without a loop. It accepts string inputs, `document`, and optional `longest_word`, which is the current longest word and defaults to an empty string.

1. [ ] Check if the first word is longer than the current `longest_word`, then recur for the rest of the document.
   - Words with equal length to `longest_word` should be skipped.
2. [ ] Ensure there are no potential [index errors](https://docs.python.org/3/library/exceptions.html#IndexError).

Assume that a "word" means a series of any consecutive non-whitespace characters. For example, `find_longest_word("How are you?")` should return the string `"you?"`.

Review the provided tests in `main_test.py` to see the expected behavior, including edge cases.

You can use [`.split`](https://docs.python.org/3/library/stdtypes.html#str.split) with `maxsplit=1`.  
That will split a string into a list of `[first_word, rest_of_string]`
