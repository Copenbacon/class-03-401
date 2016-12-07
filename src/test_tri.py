"""This tests the Trigrams module."""
import pytest

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
        "choice"]]

]


@pytest.mark.parametrize("data_list, result", DICTIONARY_TABLE)
def test_iter_over_data(data_list, result):
    """Test the iter_over_data_list function from Trigrams."""
    from trigrams import iter_over_data_list
    assert iter_over_data_list(data_list) == result


@pytest.mark.parametrize("path, result", DATA_LIST_TABLE)
def test_setup(path, result):
    """Test the setup function from Trigrams."""
    from trigrams import setup
    assert setup(path) == result
