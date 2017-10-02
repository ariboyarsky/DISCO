import numpy as np
import gensim
import sklearn
from sklearn.pipeline import Pipeline
from sklearn.ensemble import ExtraTreesClassifier

# For testing purposes we import Networking, with title Baseball
from Networking import *

n = Networking()
article = n.fetch_parsed_article("Baseball")

# This class will take in a list of tokenized words and return
# the vectorized modle using Gensim word2vec
class Vectorize:

    def __init__(self, tokens):
        model = gensim.models.Word2Vec(tokens, size=100)
        self.w2v = dict(zip(model.wv.index2word, model.wv.syn0))
        self.word2weight = None
        self.dim = len(self.w2v.items())

    def fit(self, x, y):
        tfidf = sklearn.feature_extraction.text.TfidfVectorizer(analyzer=lambda x: x)
        tfidf.fit(x)

        max_idf = max(tfidf.idf_)
        self.word2weight = sklearn.feature_extraction.text.defaultdict(
            lambda: max_idf,
            [(w, tfidf.idf_[i]) for w, i in tfidf.vocabulary_.items()])
        return self

    def transform(self, x):
        return np.array([
            np.mean([self.w2v[w] * self.word2weight[w]
                     for w in words if w in self.w2v] or
                    [np.zeros(self.dim)], axis=0)
            for words in x])



# Testing
v = Vectorize(article.words)
test = [['baseball'], ['hat'], ['yankees']]

# todo: look into word vector produced 