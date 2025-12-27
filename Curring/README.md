# Currying

Function [currying](https://en.wikipedia.org/wiki/Currying) is a specific *kind* of function transformation where we translate a single function that accepts multiple arguments into *multiple* functions that each accept a *single* argument.

This is a "normal" 3-argument function:

```py
box_volume(3, 4, 5)
```

This is a "curried" *series of functions* that does the same thing:

```py
box_volume(3)(4)(5)
```

Here's another example that includes the implementations:

```py
def sum(a, b):
  return a + b

print(sum(1, 2))
# prints 3
```

And the same thing curried:

```py
def sum(a):
  def inner_sum(b):
    return a + b
  return inner_sum

print(sum(1)(2))
# prints 3
```

The `sum` function only takes a *single* input, `a`. It returns a *new* function that takes a single input, `b`. This new function when called with a value for `b` will return the sum of `a` and `b`. *We'll talk later about why this is useful.*

## Assignment

In Doc2Doc, for some types of text files, we need to transform the font size of the text when rendering it onscreen.

Fix the `converted_font_size` function. We are using a 3rd party code library that expects our function to be a curried series of functions that each take a single argument.

- `converted_font_size` should just take a single argument, `font_size` and return a new function.
- The returned function should take a single argument, `doc_type`, and return `font_size` multiplied by the appropriate value for the given `doc_type`.

## Tip

You can always `Reset` the code to see the proper `font_size` multipliers if you accidentally change them.
