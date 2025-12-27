# Currying Practice

Markdown makes [displaying images](https://www.markdownguide.org/basic-syntax/#images-1) as simple as possible. To add an image to a markdown document, just use this syntax:

```
![alt text](url "title")
```

- `alt text` a brief description for screen readers and web scrapers. Required for accessibility.
- `url` url or relative path to image.
- `title` shown on mouse hover. Optional.

## Assignment

Doc2Doc makes using markdown a breeze. This includes adding images to markdown documents.

Complete the `create_markdown_image` function using currying. It takes a string input, `alt_text`.

1. [ ] Enclose the `alt_text` in square brackets prefixed with an exclamation point `![alt_text]`.
2. [ ] Define an inner function that also takes a string input, `url`:
   1. [ ] The inner function should first [escape](https://en.wikipedia.org/wiki/Escape_sequence) any parentheses in the URL by replacing them with [encoded sequences](https://www.url-encode-decode.com/).
      1. [ ] Use the `.replace()` string method to change any opening parenthesis `(` into `%28`.
      2. [ ] Do the same to change any closing parenthesis `)` into `%29`.
   2. [ ] Enclose the `url` with parentheses `(url)`.
   3. [ ] Add the enclosed `url` to the end of the enclosed `alt_text`: `![alt_text](url)`
   4. [ ] Define the innermost function. It should take an optional string input for the `title` (`title=None`).
      1. [ ] If a `title` is passed:
         1. [ ] Enclose it in double quotes.
         2. [ ] Then add the quoted `title` to the image syntax by first removing the closing parenthesis `)` from the end of the image syntax.
         3. [ ] Add a space and the quoted `title` with a closing parenthesis `)` to the end of the image syntax: `![alt_text](url "title")`
      2. [ ] Return the finished image syntax.
   5. [ ] Return the innermost function
3. [ ] Return the inner function
