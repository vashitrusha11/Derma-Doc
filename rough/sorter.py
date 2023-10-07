from glob import glob
import os 
import shutil
from tqdm import tqdm
import pandas as pd

csv=pd.read_csv("metadata.csv")

print(csv.iloc[:,2].value_counts())

types={"MEL": "Melanoma", 
"NV": "Melanocytic nevus", 
"BCC": "Basal cell carcinoma", 
"AKIEC": "Actinic keratosis", 
"BKL": "Benign keratosis", 
"DF": "Dermatofibroma", 
"VASC": "Vascular lesion" }

d={}

for i in tqdm(range(csv.shape[0])):
    image=(csv.iloc[i,:].values)[1]
    disease=(csv.iloc[i,:].values)[2]
    image_paths=glob(os.path.join("image",image+"*.jpg"))

    if len(image_paths)>0:
        image_path=glob(os.path.join("image",image+"*.jpg"))[0]
        final_image_path="images/"+disease+"/"+image_path.split("\\")[-1]
        # print(final_image_path)
        
        shutil.move(image_path,final_image_path)

print(d)

# data=glob(os.path.join("dataverse_files/HAM10000_images_part_1","*.jpg"))
# print(len(data))
# for i in tqdm(data):
    
    
    # image_name=str(i.split("\\")[-1]).split(".")[0]
    # masks_path=glob(os.path.join("dataverse_files/HAM10000_segmentations_lesion_tschandl",image_name+"*"))[0]
    
    # final_mask="masks/"+str(masks_path.split("\\")[-1])
    # final_image="image/"+str(i.split("\\")[-1])
    
    # shutil.move(masks_path,final_mask)
    # shutil.move(i, final_image)
    # print(masks_path)