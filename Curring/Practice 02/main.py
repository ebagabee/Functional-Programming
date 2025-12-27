def create_markdown_image(alt_text):
    alt = f"![{alt_text}]"

    def await_url(url):
        escaped_url = url.replace("(", "%28").replace(")", "%29")
        image_syntax = alt + f"({escaped_url})"
        
        def await_title(title=None):
            if not title:
                return image_syntax
            return image_syntax[:-1] + f' "{title}")'
        return await_title
    return await_url