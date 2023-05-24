from PIL import Image
import os
import glob

all_files = os.listdir("./img") # Listing all files in the "img" folder
print("{} files found.".format(len(all_files)))
non_resized_files = 0
resized_files = 0

for file in all_files:
    print("Resizing", file)
    try:
        path = "./img/"+file
        image = Image.open(path)
        
        # Setting the desired height
        new_height = 2400

        # Note that image.size returns a tuple that represents (old_width, old_height)

        # Obtaining the new_height/old_height ratio
        ratio = new_height/image.size[1]

        # Multiplying the old_width by ratio to obtain our new_width
        new_width = int(image.size[0]*ratio)

        # Resizing
        image = image.resize((new_width, new_height), Image.LANCZOS)

        path = "./result/"+file
        image.save(path)
        print("New size: {}x{} pixels.".format(image.size[0], image.size[1]))
        resized_files += 1
    except:
        print("Failed.")
        non_resized_files += 1
        pass

print("{} files resized, {} files couldn't be resized.".format(resized_files, non_resized_files))