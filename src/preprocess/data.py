# for loading/processing the images  
from keras.preprocessing.image import load_img 
from keras.preprocessing.image import img_to_array 
from keras.applications.vgg16 import preprocess_input 
# models 
from keras.applications.vgg16 import VGG16 
from keras.models import Model

model = VGG16()
model = Model(inputs = model.inputs, outputs = model.layers[-2].output)

def preprocess(path, model, is_path):
    #this dict holds all the images vectors
    datays = {}
    if is_path:
        # change the working directory to the path where the images are located
        os.chdir(path)

        # these list holds all the image filenames and vectors
        merchs = []
        
        if 'ecommerce-products-image-dataset' in path.split('/'):
            # creates a ScandirIterator aliased as files
            with os.scandir(path) as folders:
                # loops through each file in the directory
                for folder in tqdm(folders):
                    print(folder)
                    with os.scandir(path+'/'+folder.name) as fold:
                        for file in fold:
                            if file.name.endswith('.jpg'):
                                # adds only the image files to the flowers list
                                merchs.append(path+'/'+folder.name+'/'+file.name)
                                featuress = extract_features(path+'/'+folder.name+'/'+file.name, model)
                                datays[path+'/'+folder.name+'/'+file.name] = featuress
        else:
            # creates a ScandirIterator aliased as files
            with os.scandir(path) as files:
                # loops through each file in the directory
                for file in tqdm(files):
                    if file.name.endswith('.png'):
                        # adds only the image files to the list and dict
                        merchs.append(path+'/'+file.name)
                        featuress = extract_features(path+'/'+file.name, model)
                        datays[path+'/'+file.name] = featuress
    else:
        if type(path) == list:
            for i in path:
                featuress = extract_features(i, model)
                datays[i] = featuress
        else:
            featuress = extract_features(path, model)
            datays[path] = featuress
        

                    
    # get a list of the filenames
    filenmss = np.array(list(datays.keys()))
    
    # get a list of just the features
    featsss = np.array(list(datays.values()))

    # reshape so that there are 210 samples of 4096 vectors
    featsss = featsss.reshape(-1,4096)
    return filenmss, featsss