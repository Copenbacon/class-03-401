"""This tests the Trigrams module."""
import pytest

PARAMS_TABLE = [
    [],
]


@pytest.mark.parametrize("path, num_words, result", PARAMS_TABLE)
def test_main(path, num_words, result):
    """Test the main function from Trigrams."""
    from trigrams import main
    assert main(path, num_words) == result
