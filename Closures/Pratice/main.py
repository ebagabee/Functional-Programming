def new_collection(initial_docs):
    copy_initial_docs = initial_docs.copy()
    
    def inner_func(doc):
        copy_initial_docs.append(doc)
        return copy_initial_docs

    return inner_func
