"""Trigrams File to produce a trigram froma specified book.txt."""


def main(path, num_words):
    """Produce Trigrams from a path with specified number of word."""
    import io
    file = io.open(path, encoding='utf8')
    data = file.read()
    file.close()
    data_list = data.split()
    iter_over_data_list(data_list)


def iter_over_data_list(data_list):
    """Iterate over the data and add to dictionary."""
    for x in range(len(data_list) - 2):
        f = data_list[x] + ' ' + data_list[x + 1]
        dict.setdefault(f, [])
        dict[f].append(data_list[x + 2])
    return dict
