def save_model(name, model):
    # # Save machine learning model
    p = r"/kaggle/working/" + name + '.sav'
    with open(p,'wb') as filename:
        pickle.dump(model,filename)
    return p