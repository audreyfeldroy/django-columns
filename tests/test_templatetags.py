#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_templatetags
-------------------

Tests for `columns.templatetags` module.
"""

import unittest

from columns.templatetags.columns import columns


class TestColumns(unittest.TestCase):

    def test_columns(self):
        data = range(7)
        result = columns(data, 2)
        expected = [[0, 1, 2, 3], [4, 5, 6]]
        self.assertEqual(result, expected)
