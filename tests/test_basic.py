# -*- coding: utf-8 -*-
from random import randint
# from .context import hello
import unittest
from . import context
clipboard = context.clipboard


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_write_hello(self):
        random_num = randint(0,100000000)
        st = str(random_num)
        clipboard.clipboard_write_to_clipboard(st)

        assert st == clipboard.clipboard_read_from_clipboard()


if __name__ == '__main__':
    unittest.main()
