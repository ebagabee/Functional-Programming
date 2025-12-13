def sum_nested_list(lst):
    total_size = 0
    
    for item in lst:
        if isinstance(item, list):
            total_size += sum_nested_list(item)
        else:
            total_size += item
            
    return total_size