# -*- coding: utf-8 -*-

"""JSON files diff test."""

from gendiff.gener_diff import generate_diff
import tests.expected as expected


def test_plain():
    result = generate_diff('./tests/fixtures/big1.json',
                           './tests/fixtures/big2.json',
                           'json')
    assert result == expected.JSON
