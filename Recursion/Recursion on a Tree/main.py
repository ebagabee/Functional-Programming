def list_files(parent_directory, current_filepath=""):
    file_paths = []

    for key in parent_directory.keys():
        filepath = current_filepath + "/" + key
        
        if parent_directory[key] is None:
            file_paths.append(filepath)
        else:
            result = list_files(parent_directory[key], filepath)
            file_paths.extend(result)


    return file_paths