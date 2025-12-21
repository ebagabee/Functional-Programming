def get_filter_cmd(filter_one, filter_two):
    def filter_cmd(content, option = "--one"):
        if option == "--one":
            return filter_one(content)

        if option == "--two":
            return filter_two(content)

        if option == "--three":
            result_one = filter_one(content)

            return filter_two(result_one)

        raise Exception("invalid option")

    return filter_cmd

def replace_bad(text):
    return text.replace("bad", "good")


def replace_ellipsis(text):
    return text.replace("..", "...")


def fix_ellipsis(text):
    return text.replace("....", "...")
