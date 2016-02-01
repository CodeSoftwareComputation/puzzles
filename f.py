def rewrite(document, filter_words):
    for string in document.split():
        if string not in filter_words:
            print string
        else:
            print string[0] + "*" * len(string[1:])
