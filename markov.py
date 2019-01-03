from re import findall
from random import choice
from collections import defaultdict, deque

d_re_pattern = r"([\w\.,!?']+|[\n]+)"
d_break_string = "\n\n"
d_re_flags = 0
d_whitespace = " "


class MarkovChain(object):
    def __init__(self, string, break_string=d_break_string,
                 re_pattern=d_re_pattern, re_flags=d_re_flags,
                 whitespace=d_whitespace):
        self.whitespace = whitespace
        self.train(string, break_string, re_pattern, re_flags)

    def train(self, string, break_string=d_break_string,
              re_pattern=d_re_pattern, re_flags=d_re_flags):

        self.break_string = break_string

        words = findall(re_pattern, string, re_flags)
        words_iter = iter(words)

        connections = defaultdict(list)
        previous_word = next(words_iter)
        connections[break_string] = [previous_word]

        for w in words:
            connections[previous_word].append(w)
            previous_word = w

        self.connections = connections

    def predict(self, n=1, start=None):
        if start is None:
            last_word = self.break_string
            words = deque()
        else:
            # only add the starting word to the beginning if it's not a break
            last_word = start
            words = deque([last_word])
            n -= 1


        for i in range(n):
            new_word = choice(self.connections[last_word])
            words.append(new_word)
            last_word = new_word

        return self.whitespace.join(words)
