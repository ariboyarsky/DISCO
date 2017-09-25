import gensim
import numpy as np
from sklearn import feature_extraction

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

    def fit(self, x, y):
        tfidf = TfidfVectorizer(analyzer=lambda x: x)
        tfidf.fit(x)

        max_idf = max(tfidf.idf_)
        self.word2weight = defaultdict(
            lambda: max_idf,
            [(w, tfidf.idf_[i]) for w, i in tfidf.vocabulary_.items()])
        return self

    def transform(self, x):
        return np.array([
            np.mean([self.w2v[w] * self.word2weight[w]
                     for w in words if w in self.w2v] or
                    [np.zeros(self.dim)], axis=0)
            for words in x])



