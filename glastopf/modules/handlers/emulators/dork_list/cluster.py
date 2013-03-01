from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans


class Cluster(object):
    def __init__(self, pattern, n_clusters, max_iter, n_init, min_df=2):
        self.pattern = pattern
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.n_init = n_init
        self.min_df = min_df

    def preprocessor(self, url):
        url = str(url)
        url = url.lower()
        url += '/'
        return url

    def write_clusters(self, url_list, labels):
        clusters = {}
        for url, label in zip(url_list, labels):
            if label in clusters:
                clusters[label].append(url)
            else:
                clusters[label] = [url]
        return clusters

    def cluster(self, url_list):
        vectorizer = CountVectorizer(preprocessor=self.preprocessor, token_pattern=self.pattern, min_df=self.min_df)
        X = vectorizer.fit_transform(url_list)
        km = KMeans(n_clusters=self.n_clusters, max_iter=self.max_iter, verbose=0, n_init=self.n_init,
                    precompute_distances=True)
        km.fit(X)
        return self.write_clusters(url_list, km.labels_)
