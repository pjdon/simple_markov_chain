from markov import MarkovChain, d_re_pattern, d_re_flags
import unittest
from re import findall


class MarkovTests(unittest.TestCase):
    # setup chain object
    source_file = "the_black_cat.txt"
    with open(source_file, encoding="utf-8") as f:
        text = f.read()
    m = MarkovChain(text)

    def test_start(self):
        """Check that the correct start is used"""
        start = "From"
        predicted = self.m.predict(20, start)
        self.assertTrue(predicted.startswith(start))
        pass

    def test_length(self):
        """Check that the chain outputs the correct number of words"""
        n = 100
        predicted = self.m.predict(100)
        tokens = findall(d_re_pattern, predicted, d_re_flags)
        expected = n
        actual = len(tokens)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
