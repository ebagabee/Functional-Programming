def word_count_aggregator():
    count = 0
    
    def inner_func(doc):
        nonlocal count

        doc_array = doc.split()
        length = len(doc_array)

        count += length
        return count

    return inner_func