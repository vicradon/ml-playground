def predict(image_name, mod, grp, kms):
    f_names, feats = preprocess(image_name, mod, False)
    #Predict Cluster
    prediction = kms.predict(feats)
    #This holds the predicted cluster id and the image path
    grups = {}
    #This holds the similar images from the dataset
    grpp = {}
    for file, cluster in zip(f_names, prediction):
        if cluster not in grups.keys():
            grups[cluster] = []
            grpp[cluster] = grp[cluster]
            grups[cluster].append(file)
        else:
            grups[cluster].append(file)
            
    return grups, grpp