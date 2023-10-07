import cv2
import numpy as np
import matplotlib.pyplot as plt

def bounding_box(image_path,mask_path,
                 label, 

                            padding=10, 
                            rectangle_thickness=4, 
                            rectangle_color=(0, 0, 255),
                            font = cv2.FONT_HERSHEY_SIMPLEX,           
                            font_scale=1, 
                            font_thickness=2, 
                            font_color=(255, 255, 255), 
                            background_color=(0, 0, 255)):

    label_background_padding = 12

    image=cv2.imread(image_path)
    mask = cv2.imread(mask_path)

    gray = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

    # Threshold the image
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Find contours
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Calculate label size for background rectangle
    (text_width, text_height), _ = cv2.getTextSize(label, font, font_scale, font_thickness)
    

    # Draw bounding boxes with padding, label background, and label
    
    for contour in contours[-1:]:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(image, (x-padding, y-padding), (x+w+padding, y+h+padding), rectangle_color, rectangle_thickness)
        
        # Draw label background
        cv2.rectangle(image, 
                    (x-padding-2, y+h+padding), 
                    (x-padding + text_width + label_background_padding, y+h+padding+text_height+label_background_padding), 
                    background_color, -1)  # -1 fills the rectangle
        
        # Draw label
        cv2.putText(image, label, (x-padding, y+h+padding+text_height+2), 
                    font, font_scale, font_color, font_thickness)

    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Test the function with the given image

# processed_image = bounding_box("data\\images\\akiec\\ISIC_0025247.jpg","data\\masks\\ISIC_0025247_segmentation.png","sexsumxsnjf")
# plt.figure(figsize=(10, 10))
# plt.imshow(processed_image)
# # plt.imshow()
# plt.axis('off')
# plt.show()
