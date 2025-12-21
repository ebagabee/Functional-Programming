def doc_format_checker_and_converter(conversion_function, valid_formats):
    def check_and_convert(filename, content):
        suffix = filename.split(".")[1]

        if suffix not in valid_formats:
            raise ValueError("invalid file format")

        return conversion_function(content)
        

    return check_and_convert

def capitalize_content(content):
    return content.upper()


def reverse_content(content):
    return content[::-1]
