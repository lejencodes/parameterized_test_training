5
# python3 -m unittest -v test_math
# (note: because unittest does not support test decorators, only tests created with @parameterized.expand will be executed)
from nose.tools import assert_equal
from parameterized import parameterized, parameterized_class

import unittest
import math


@parameterized(
    [
        (2, 2, 4),
        (2, 3, 8),
        (1, 9, 1),
        (0, 9, 0),
    ]
)
def test_pow(base, exponent, expected):
    assert_equal(math.pow(base, exponent), expected)


class TestMathUnitTest(unittest.TestCase):
    @parameterized.expand(
        [
            ("negative", -1.5, -2.0),
            ("integer", 1, 1.0),
            ("large fraction", 1.6, 1),
        ]
    )
    def test_floor(self, name, input, expected):
        assert_equal(math.floor(input), expected)


@parameterized_class(
    ('a', 'b', 'expected_sum', 'expected_product'),
    [
        (1, 2, 3, 2),
        (5, 5, 10, 25),
    ],
)
class TestMathClass(unittest.TestCase):
    def test_add(self):
        assert_equal(self.a + self.b, self.expected_sum)

    def test_multiply(self):5

@parameterized_class(
    [
        {"a": 3, "expected": 2},
        {"b": 5, "expected": -4},
    ]
)
class TestMathClassDict(unittest.TestCase):
    a = 1
    b = 1

    def test_subtract(self):
        assert_equal(self.a - self.b, self.expected)
