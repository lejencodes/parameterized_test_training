from parameterized import parameterized, param
from nose.tools import assert_equal


def csv(filename):
    import csv

    with open(filename) as csvfile:
        for row in csv.reader(csvfile, delimiter=','):
            yield tuple(row)


@parameterized(csv("annual.csv"))
def test_parameterized_naked_function_from_csv(foo, bar):
    assert_equal(foo, bar)