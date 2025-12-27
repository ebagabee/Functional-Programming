# Currying Practice

Doc2Doc should include a feature for image resizing, allowing users to adjust image dimensions to specified ranges. This ensures that images in documents fit and aren't freakishly large or hilariously small.

## Assignment

Complete the `new_resizer` function using currying. It should make sure the image dimensions are never smaller than the minimum width and height, or larger than the maximum width and height specified.

Check the example at the bottom to see how it is intended to be called.

1. [ ] In the `new_resizer` body, define an inner function that takes two optional integer inputs `min_width` and `min_height` with default values of `0`, and in its body:
   1. [ ] If `min_width` is more than `max_width` or `min_height` is more than `max_height`, raise an exception `"minimum size cannot exceed maximum size"`.
   2. [ ] Define an innermost function that takes two integer inputs `width` and `height`, and in its body:
      1. [ ] Use the built-in [`min`](https://docs.python.org/3/library/functions.html#min) and [`max`](https://docs.python.org/3/library/functions.html#max) functions to reduce `width` if it's above `max_width` or increase it if it's below `min_width`.
      2. [ ] Do the same for `height`.
      3. [ ] Return the new `width` and `height`.
   3. [ ] Return the innermost function.
2. [ ] Return the inner function.

## Example

If our `new_resizer` function returns a `set_min_size` function, and `set_min_size` returns a `resize_image` function, we would use it like this:

```py
# Step 1: Create the resizer with maximum dimensions
set_min_size = new_resizer(800, 600)

# Step 2: Set the minimum dimensions
resize_image = set_min_size(200, 100)

# Step 3: Resize the image
new_width, new_height = resize_image(1000, 500)

# Step 4: Output the result
print(new_width, new_height)  # Output: 800, 500

# With currying syntax
print(new_resizer(800, 600)(200, 100)(1000, 500))  # Output: (800, 500)
```
