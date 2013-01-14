from ConfigParser import ConfigParser

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans


class Cluster(object):

    def __init__(self):
        pass

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

    def cluster(self, url_list, config):
        conf_parser = ConfigParser()
        conf_parser.read(config)
        vectorizer = CountVectorizer(preprocessor=self.preprocessor, token_pattern=conf_parser.get('dork-db', 'token_pattern'))
        X = vectorizer.fit_transform(url_list)
        n_clusters = conf_parser.getint('dork-db', 'n_clusters')
        max_iter = conf_parser.getint('dork-db', 'max_iter')
        n_init = conf_parser.getint('dork-db', 'n_init')
        km = KMeans(n_clusters=n_clusters, max_iter=max_iter, verbose=0, n_init=n_init, precompute_distances=True)
        km.fit(X)
        self.clusters = self.write_clusters(url_list, km.labels_)
