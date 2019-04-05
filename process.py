from PIL import Image, ImageFile
import os.path as path
import os

def process(path_name):
    folder = path_name
    last_path_name = os.path.basename(os.path.normpath(path_name))
    count = 0
    for file in os.listdir(folder):
        filename = file
        print filename
        ImageFile.LOAD_TRUNCATED_IMAGES = True
        image = Image.open(path_name + '/' + filename)
        #make sure the images are the same filetype
        if (image.format) != 'PNG':
            image.format = 'PNG'

        #make sure the images are of the same mode
        if (image.mode) != 'RGB':
            image.mode = 'RGB'

        #resizing the image
        tn_image = image.resize((400, 400))
        greyscale_image = tn_image.convert('L')

        two_up = path.abspath(path.join(path_name,"../.."))
        #Saving the images
        greyscale_image.save(two_up + "/Processed/train/{}/image{}.png".format(last_path_name,count+1))
        count += 1

def seperate_train_test_data():
   import shutil
   import numpy as np

   base_dir = os.getcwd()

   if (os.path.exists("\\Processed\\validate\\hotels") == False):
       os.makedirs(base_dir +"\\Processed\\validate\\hotels", 0755)
   if (os.path.exists("\\Processed\\validate\\not-hotels") == False):
       os.makedirs(base_dir + "\\Processed\\validate\\not-hotels", 0755)

   
   sourceN = base_dir + "\\Processed\\train\\hotels"
   destN = base_dir + "\\Processed\\validate\\hotels"
   sourceP = base_dir + "\\Processed\\train\\not-hotels"
   destP = base_dir + "\\Processed\\validate\\not-hotels"

   filesN = os.listdir(sourceN)
   filesP = os.listdir(sourceP)       

   for f in filesN:
        if np.random.rand(1) < 0.2:
            shutil.move(sourceN + '\\'+ f, destN + '\\'+ f)
   for i in filesP:
        if np.random.rand(1) < 0.2:
            shutil.move(sourceP + '\\'+ i, destP + '\\'+ i)

   print(len(os.listdir(sourceN)))
   print(len(os.listdir(sourceP)))
   print(len(os.listdir(destN)))
   print(len(os.listdir(destP)))



process('training_images/hotels')
process('training_images/not-hotels')
#seperate_train_test_data()

 
