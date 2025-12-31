# Args and Kwargs

In Python, [`*args` and `**kwargs`](https://book.pythontips.com/en/latest/args_and_kwargs.html) allow a function to accept and deal with a *variable* number of arguments.

- `*args` collects positional arguments into a *tuple*
- `**kwargs` collects keyword (named) arguments into a *dictionary*

```py
def print_arguments(*args, **kwargs):
    print(f"Positional arguments: {args}")
    print(f"Keyword arguments: {kwargs}")

print_arguments("hello", "world", a=1, b=2)
# Positional arguments: ('hello', 'world')
# Keyword arguments: {'a': 1, 'b': 2}
```

## Positional Arguments

Positional arguments are the ones you're already familiar with, where the order of the arguments matters. Like this:

```py
def sub(a, b):
    return a - b

# a=3, b=2
res = sub(3, 2)
# res = 1
```

## Keyword Arguments

[Keyword arguments](https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments) are passed in by name. *Order does not matter*. Like this:

```py
def sub(a, b):
    return a - b

res = sub(b=3, a=2)
# res = -1
res = sub(a=3, b=2)
# res = 1
```

## A Note on Ordering

Any positional arguments *must come before* keyword arguments. This will *not* work:

```py
sub(b=3, 2)
```

## Assignment

At Doc2Doc, we need better internal debugging tools. **Complete the `args_logger` function.** It takes a variable number of positional and keyword arguments and prints them to the console.

1. [ ] Print each positional argument *sequentially* using numbers and periods as list markers, starting with `1.` . For example:

```py
args_logger("what's", "up", "doc")
```

prints to the console:

```
1. what's
2. up
3. doc
```

2. [ ] Sort the keyword argument *alphabetically by key* with the [`sorted`](https://docs.python.org/3/library/functions.html#sorted) function.
3. [ ] Then print the sorted keyword arguments using asterisks (`*`) as list markers, and with a colon (`:`) between the key and value. For example:

```py
args_logger("hi", "there", age=17, date="July 4 1776")
```

prints to the console:

```
1. hi
2. there
* age: 17
* date: July 4 1776
```

## Tips

- Don't feel guilty about using loops.
- `kwargs` is a dictionary, not a list. My recommendation is to use the [`.items()`](https://docs.python.org/3/library/stdtypes.html#dict.items) method to get the key-value pairs as a list of tuples, then sort that list before printing.
- When you call `sorted` on a list of tuples, by default it sorts by the first item in each tuple (which is what you want here).
