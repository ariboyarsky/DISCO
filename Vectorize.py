import gensim

# For testing purposes we import Networking, with title Baseball
import Networking

n = Networking()
n.fetch_parsed_article("Baseball")

# This class will take in a list of tokenized words and return
# the vectorized modle using Gensim word2vec
class Vectorize:

    def __init__(self, tokens):
        model = gensim.models.word2vec(tokens, size=100)
        self.w2v = dict(zip(model.wv.index2word, model.wv.syn0))
        self.word2weight = None
        self.dim = len(self.w2v.itervalues().next())

    def fit(self):
        return self
