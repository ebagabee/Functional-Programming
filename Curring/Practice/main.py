from functools import reduce

def lines_with_sequence(char):
    def with_char(length):
        sequence = char * length

        def with_length(doc):
            doc_array = doc.split("\n")
            accumulator = reduce(
                lambda count, item: count + (1 if sequence in item else 0),
                doc_array,
                0
            )
            
            return accumulator

        return with_length
    return with_char