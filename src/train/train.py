# clustering and dimension reduction
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

def train(filenms, featsss, clust=10):
    # cluster feature vectors
    kmeansss = KMeans(n_clusters=clust, random_state=22)
    kmeansss.fit(featsss)


    # holds the cluster id and the images { id: [images] }
    grops = {}
    for file, cluster in zip(filenms,kmeansss.labels_):
        if cluster not in grops.keys():
            grops[cluster] = []
            grops[cluster].append(file)
        else:
            grops[cluster].append(file)
    return grops, kmeansss