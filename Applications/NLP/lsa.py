class LSA(object):
    def __init__(self):
        pass


from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import Normalizer
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
vec = TfidfVectorizer()
corpus = ['This is sample document.', 'another random document.', 'third sample document text']

svd = TruncatedSVD(2)
norm = Normalizer(copy = False)
lsa = make_pipeline(svd, norm)

X = vec.fit_transform(corpus)
X = lsa.fit_transform(X)
print svd.explained_variance_ratio_.sum()

print svd.explained_variance_ratio_
print X
print svd.components_