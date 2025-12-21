# Closure Practice

Remember, a [closure](https://en.wikipedia.org/wiki/Closure_\(computer_programming\)) is a function that retains the state of its environment. That makes it useful for tracking data as it changes over time, but it can come at the cost of understandability.

When not to use the `nonlocal` keyword: when the variable is mutable (such as a list, dictionary or set), and you are modifying its contents rather than reassigning the variable. You only need the `nonlocal` keyword if you are reassigning a variable instead of modifying its contents (which you must do to change immutable values such as strings and integers).

Let's try a closure without the `nonlocal` keyword.

## Assignment

Complete the `new_collection` function. It takes as input:

- `initial_docs`: a list of strings.

It returns a function that:

1. [ ] Accepts a string
2. [ ] _Closes over_ a **copy** of `initial_docs`.
3. [ ] Appends the input to the closed-over list
4. [ ] Returns the updated list.

**Do not** modify the original `initial_docs` list!

## Example Usage

```py
my_collection = new_collection(["doc1", "doc2", "doc3"])
print(my_collection("doc4"))
# ['doc1', 'doc2', 'doc3', 'doc4']
print(my_collection("doc5"))
# ['doc1', 'doc2', 'doc3', 'doc4', 'doc5']
```