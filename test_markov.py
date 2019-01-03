from markov import MarkovChain

source_file = "the_black_cat.txt"
with open(source_file, encoding="utf-8") as f:
    text = f.read()

m = MarkovChain(text)
print(m.predict(1000))
