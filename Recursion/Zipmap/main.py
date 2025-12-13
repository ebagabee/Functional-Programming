def zipmap(keys, values):
    if len(keys) == 0 or len(values) == 0:
        return {}
    
    zipmap(keys[1:], values[1:])