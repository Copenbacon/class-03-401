"""This tests the Trigrams module."""
import pytest

MAIN_TABLE = [
    ['src/texts/sample.txt', 400, 400],
    ['src/texts/pride_prejudice.txt', 250, 250],
]


DATA_LIST_TABLE = [
    ["src/texts/simple_test.txt", [
        "holy",
        "shit,",
        "it's",
        "fucking",
        "butter"]],
    ["src/texts/simple_test2.txt", [
        "pride",
        "and",
        "prejudice",
        "is",
        "our",
        "book",
        "of",
        "choice"]],
]

DICTIONARY_TABLE = [
    [["holy", "shit", "it's", "butter"], {
        'holy shit': ['it\'s'],
        'shit it\'s': ['butter'],
    }],
    [["holy", "shit", "it's", "fucking", "butter"], {
        'holy shit': ['it\'s'],
        'shit it\'s': ['fucking'],
        'it\'s fucking': ['butter']
    }],
]

FIRST_VALUES_TABLE = [
    [{
        'holy shit': ['it\'s'],
    }, ["holy", "shit", "it's"]
    ],

    [{
        'shit it\'s': ['butter'],
    }, ["shit", "it's", "butter"]
    ],

    [{
        'it\'s fucking': ['butter'],
    }, ["it's", "fucking", "butter"]
    ],
]

GENERATE_TEXT_TABLE = [
    [["shit", "it's", "butter"], {
        'holy shit': ['it\'s'],
        'shit it\'s': ['butter'],
    }, 5],
    [["holy", "shit", "it's"], {
        'holy shit': ['it\'s'],
        'shit it\'s': ['butter'],
    }, 10],
]

WRITE_SCREEN_TABLE = [
    [["holy", "shit", "it's", "butter"], "holy shit it's butter "],
    [["holy", "shit", "it's", "fucking", "butter"], "holy shit it's fucking butter "],
]


@pytest.mark.parametrize("path, num_words, result", MAIN_TABLE)
def test_main(path, num_words, result):
    """Test the setup function from Trigrams."""
    from trigrams import main
    assert len(main(path, num_words).split()) == result


@pytest.mark.parametrize("path, result", DATA_LIST_TABLE)
def test_setup(path, result):
    """Test the setup function from Trigrams."""
    from trigrams import setup
    assert setup(path) == result


@pytest.mark.parametrize("data_list, result", DICTIONARY_TABLE)
def test_iter_over_data(data_list, result):
    """Test the iter_over_data_list function from Trigrams."""
    from trigrams import iter_over_data_list
    assert iter_over_data_list(data_list) == result


@pytest.mark.parametrize("some_dict, result", FIRST_VALUES_TABLE)
def test_generate_first_values(some_dict, result):
    """Test Generate First Values func is outputting first values."""
    from trigrams import generate_first_values
    assert(generate_first_values(some_dict)) == result


@pytest.mark.parametrize("text, special_dict, num_words", GENERATE_TEXT_TABLE)
def test_generate_text(text, special_dict, num_words):
    """Test Generate Text function is outputting correct num_words."""
    from trigrams import generate_text
    assert len(generate_text(text, special_dict, num_words)) == num_words


@pytest.mark.parametrize("text, result", WRITE_SCREEN_TABLE)
def test_write_text_to_screen(text, result):
    """Test that text should write to screen."""
    from trigrams import write_text_to_screen
    assert write_text_to_screen(text) == result
