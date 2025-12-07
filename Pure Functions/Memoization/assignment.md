# Memoization

At its core, [memoization](https://en.wikipedia.org/wiki/Memoization) is just [caching](<https://en.wikipedia.org/wiki/Cache_(computing)>) (storing a copy of) the result of a computation so that we don't have to compute it again in the future.

For example, take this simple function:

```py
def add(x, y):
    return x + y
```

A call to `add(5, 7)` will *always* evaluate to `12`. So, if you think about it, once we know that `add(5, 7)` can be replaced with `12`, we can just store the value `12` somewhere in memory so that we don't have to do the addition operation again in the future. Then, if we need to `add(5, 7)` again, we can just look up the value `12` instead of doing a (potentially expensive) CPU operation.

The slower and more complex the function, the more memoization can help speed things up.

It's pronounced "memOization", not "memORization". This confused me for quite a while in college, I thought my professor just didn't speak goodly...

## Assignment

Counting the words in a document can be slow, so we want to *memoize* it.

Complete the `word_count_memo` function. It takes two inputs:

1. A `document` string.
2. A `memos` dictionary. The keys are full document strings, and the values are the word count of the document.

It should return two values:

1. The word count of the given document
2. An updated `memos` dictionary.

Here are the steps to follow:

1. [ ] Create a [.copy()](https://docs.python.org/3/library/copy.html#module-copy) of the `memos` dictionary.
2. [ ] If the document is [in](https://docs.python.org/3/library/stdtypes.html#dict) the `memos` dictionary, just `return` the associated word count and the `memos` copy. No need to recompute the word count.
3. [ ] Otherwise, use the provided `word_count` function to count the words in the given `document`.
4. [ ] Store the word count in the `memos` copy.
5. [ ] `return` the word count and the updated `memos` copy.
