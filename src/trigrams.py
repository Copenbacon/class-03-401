"""Trigrams File to produce a trigram froma specified book.txt."""


def main(path, num_words):
    """Produce Trigrams from a path with specified number of word."""
    data_list = setup(path)
    dict_of_pp = iter_over_data_list(data_list)
    text = generate_first_values(dict_of_pp)
    text = generate_text(text, dict_of_pp, num_words)
    printme = write_text_to_screen(text)
    return printme


def setup(path):
    """Setup the file to render a list of words from the file in the path."""
    import io
    file = io.open(path, encoding='utf8')
    data = file.read()
    file.close()
    data_list = data.split()
    return data_list


def iter_over_data_list(data_list):
    """Iterate over the data and add to dictionary."""
    dict_of_pp = {}
    for x in range(len(data_list) - 2):
        f = data_list[x] + ' ' + data_list[x + 1]
        dict_of_pp.setdefault(f, [])
        dict_of_pp[f].append(data_list[x + 2])
    return dict_of_pp


def generate_first_values(dict_of_pp):
    """Generate the first key and values to write to the file."""
    import random
    text = []
    rand_key = random.choice(list(dict_of_pp.keys()))
    first_word_pair = rand_key.split()
    text.extend(first_word_pair)
    rand_num = random.randint(0, len(dict_of_pp[rand_key]) - 1)
    new_word = dict_of_pp[rand_key][rand_num]
    text.append(new_word)
    return text


def generate_text(text, dict_of_pp, num_words):
    """Generate the text to write to the file."""
    import random
    while len(text) < num_words:
        try:
            new_word_pair = text[-2] + ' ' + text[-1]
            rand_num4 = random.randint(0, len(dict_of_pp[new_word_pair]) - 1)
            new_word = dict_of_pp[new_word_pair][rand_num4]
            text.append(new_word)
        except KeyError:
            new_word_pair = random.choice(list(dict_of_pp.keys()))
            text.append(new_word_pair)
    return text


def write_text_to_screen(text):
    """Write the text to the user's screen."""
    the_written_word = ''
    for i in range(len(text)):
        the_written_word += text[i] + ' '
    return the_written_word


if __name__ == "__main__":
    import sys
    user_input1 = sys.argv[1]
    user_input2 = sys.argv[2]
    print(main(user_input1, int(user_input2)))
