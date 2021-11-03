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
    - Convert number divisible by 5 to "Chinos"
    - Convert number divisible by 3 and 5 to "Vino Chinos"
2. List mapper:
    √ Can call
    - Return converted list when given an integer list
3. Printer:
    √ Can call
    - Given an empty list, print an error message
    - Given a list, prints expected values

"""
from vino_chinos import vino_chino_converter, vino_chino_mapper, vino_chino_printer


def test_vino_chino_converter_1():
    vc = vino_chino_converter(1)
    assert vc == "1"


def test_vino_chino_converter_2():
    vc = vino_chino_converter(2)
    assert vc == "2"


def test_vino_chino_converter_3():
    vc = vino_chino_converter(3)
    assert vc == "Vino"


def test_vino_chino_converter_6():
    vc = vino_chino_converter(6)
    assert vc == "Vino"


def test_can_call_vino_chino_mapper():
    vc_list = vino_chino_mapper([])


def test_can_call_vino_chino_printer():
    vino_chino_printer([])
