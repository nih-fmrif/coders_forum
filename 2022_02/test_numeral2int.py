"""Tests for numeral2int"""

from numeral2int import numeral2int
import pytest


def tests_numeral2int_fails():
    """numeral2int fails in the expected ways"""
    with pytest.raises(ValueError, match=r"Invalid"):
        numeral2int("P")

    with pytest.raises(ValueError, match=r"Empty Roman numeral"):
        numeral2int("")

def test_numeral2int_succeeds():
    """numeral2int works!"""
    # one-character test
    assert numeral2int("I") == 1
    assert numeral2int("C") == 100

    # subtractive notation test
    assert numeral2int("IX") == 9
