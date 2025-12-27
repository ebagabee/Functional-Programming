def new_resizer(max_width, max_height):
    def min_resize(min_width = 0, min_height = 0):
        if min_width > max_width or min_height > max_height:
            raise Exception("minimum size cannot exceed maximum size")

        def resize(width, height):             
            if width > max_width:
                width = min(width, max_width)

            if width < min_width:
                width = max(width, min_width)

            if height > max_height:
                height = min(height, max_height)

            if (height < min_height):
                height = max(height, min_height)

            return (width, height)
            
        return resize
        
    return min_resize
