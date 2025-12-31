def args_logger(*args, **kwargs):
    args_to_array = list(args)

    if len(args_to_array) > 0:
        for index, value in enumerate(args_to_array):
            print(f"{index + 1}. {value}")

    for key, value in sorted(kwargs.items()):
       print(f"* {key}: {value}")