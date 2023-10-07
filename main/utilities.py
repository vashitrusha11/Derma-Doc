import pandas as pd
from glob import glob
import os 

def get_image_path(image_name):
    image_path=glob(os.path.join("D:/Projects/Hack-for-india/ham_data/images","*",image_name))
    return image_path[0]

def get_mask_path(image_name):
    mask_path=glob(os.path.join("D:/Projects/Hack-for-india/ham_data/masks/",image_name.split(".")[0]+"*"))
    
    return mask_path[0]

# ="data\\images\\akiec\\ISIC_0025247.jpg"
# image_path=get_mask_path("ISIC_0025247.jpg")
# print(image_path)
# data=pd.read_csv("metadata.csv")
# print(get_disease_name("ISIC_0025247.jpg"))

def get_disease_name(image_name):
    data=pd.read_csv("D:/Projects/Hack-for-india/metadata.csv")
    disease_types={
    "mel": "Melanoma", 
    "nv": "Melanocytic nevus", 
    "bcc": "Basal cell carcinoma", 
    "akiec": "Actinic keratosis", 
    "bkl": "Benign keratosis", 
    "df": "Dermatofibroma", 
    "vasc": "Vascular lesion" }

    image_name=image_name.split(".")[0]
 
    data_list=(data.loc[data['image_id'] == image_name].values[0])
    
    name=disease_types[data_list[2]]

    return name
