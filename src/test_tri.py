"""This tests the Trigrams module."""
import pytest

PARAMS_TABLE = [
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


@pytest.mark.parametrize("data_list, result", PARAMS_TABLE)
def test_iter_over_data(data_list, result):
    """Test the main function from Trigrams."""
    from trigrams import iter_over_data_list
    assert iter_over_data_list(data_list) == result
