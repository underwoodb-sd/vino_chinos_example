"""Test module for vino_chinos.py

Features:
1. Convert an integer to a string, based on the vino chinos algorithm.
2. Map this converter to a list of numbers
3. Print out mapped list

Test Cases:
1. Vino chinos converter:
    √ Can call
    √ Convert regular number to string
    √ Convert number divisible by 3 to "Vino"
    √ Convert number divisible by 5 to "Chinos"
    √ Convert number divisible by 3 and 5 to "Vino Chinos"
2. List mapper:
    √ Can call
    - Return converted list when given an integer list
3. Printer:
    √ Can call
    - Given an empty list, print an error message
    - Given a list, prints expected values

"""
from vino_chinos import vino_chino_converter, vino_chino_mapper, vino_chino_printer
import pytest


converter_test_cases = [
    (1, "1"),
    (2, "2"),
    (3, "Vino"),
    (5, "Chinos"),
    (6, "Vino"),
    (10, "Chinos"),
    (15, "Vino Chinos"),
    (30, "Vino Chinos"),
]


@pytest.mark.parametrize("input,expected", converter_test_cases)
def test_vino_chino_converter(input, expected):
    vc = vino_chino_converter(input)
    assert vc == expected


def test_vino_chino_converter_10():
    vc = vino_chino_converter(10)
    assert vc == "Chinos"


def test_can_call_vino_chino_mapper():
    vc_list = vino_chino_mapper([])


def test_can_call_vino_chino_printer():
    vino_chino_printer([])
