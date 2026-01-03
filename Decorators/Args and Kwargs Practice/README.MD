# Args and Kwargs Practice

Doc2Doc should be extensible to allow for third-party plugins. These plugins will be configurable.

## Assignment

Complete the `configure_plugin_decorator` function. It decorates a `func` that takes keyword arguments `**kwargs`, but the wrapper function it returns takes positional arguments `*args`. The arguments passed to the wrapper will be a series of tuples, each a key/value pair.

1. [ ] Create a wrapper function that takes positional arguments `*args`:
   1. [ ] Within the wrapper function, convert the `args` into a dictionary with the [`dict`](https://docs.python.org/3/library/stdtypes.html#dict) function.
   2. [ ] Return the result of passing this dictionary into `func` as keyword arguments using the `**` operator to [unpack the dict](https://www.bitecode.dev/i/140708565/unpacking-arguments).
2. [ ] Return the wrapper function.

```python
plugin_config = configure_backups(("path", "~/duplicates"), ("prefix", "duplicate_"), ("extension", ".rtf"))

# plugin_config:
# {
#   "path": "~/duplicates",
#   "prefix": "duplicate_",
#   "extension": ".rtf",
# }
```
