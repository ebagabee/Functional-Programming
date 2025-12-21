import copy

def css_styles(initial_styles):
    copy_initial_styles = copy.deepcopy(initial_styles)
    
    def add_style(selector, property, value):
        if selector not in copy_initial_styles:
            copy_initial_styles[selector] = {}

        copy_initial_styles[selector][property] = value
        return copy_initial_styles

    return add_style