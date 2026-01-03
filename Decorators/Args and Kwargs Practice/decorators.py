def configure_plugin_decorator(func):
    def inner_func(*args):
        return func(**dict(args))
    
    return inner_func