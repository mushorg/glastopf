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
        cluster_sizes = []
        for url, label in zip(url_list, labels):
            if label in clusters:
                clusters[label].append(url)
            else:
                clusters[label] = [url]
        return clusters

    def print_clusters(self, clusters):
        for label, urls in clusters.items():
            print "Cluster {0}:".format(label)
            for url in urls:
                print "\t", url

    def cluster(self, url_list, config):
        conf_parser = ConfigParser()
        conf_parser.read(config)
        vectorizer = CountVectorizer(preprocessor=self.preprocessor, token_pattern=conf_parser.get('dork-db', 'token_pattern'))
        X = vectorizer.fit_transform(url_list)
        km = KMeans(n_clusters=30, max_iter=50, verbose=0, n_init=20)
        km.fit(X)
        self.clusters = self.write_clusters(url_list, km.labels_)
        """max_cluster_label = max(self.clusters.items(), key=lambda x: len(x[1]))[0]
        rem_url_list = clusters[max_cluster_label]
        del clusters[max_cluster_label]

        X = vectorizer.fit_transform(rem_url_list)
        km = KMeans(n_clusters=5, max_iter=50, verbose=0, n_init=20)
        km.fit(X)
        clusters_2 = self.write_clusters(rem_url_list, km.labels_)"""

        #self.print_clusters(self.clusters)
        #self.print_clusters(clusters_2)
