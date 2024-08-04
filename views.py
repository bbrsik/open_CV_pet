import os
import cv2
from settings import ASSETS_DIR
from utility import should_rename_files_in_folder, rename_files_in_folder


def display_images(folder: str):
    if should_rename_files_in_folder(ASSETS_DIR):
        rename_files_in_folder(ASSETS_DIR)
        print(f"Finished renaming files in folder: '{ASSETS_DIR}'.")

    images = os.listdir(ASSETS_DIR)
    if len(images) == 0:
        print("Notice:")
        print(f"Folder '{ASSETS_DIR}' is empty!")
        return -1

    print(f"Displaying images in folder: '{ASSETS_DIR}'.")
    for img_name in images:
        print(f"Displaying {img_name}...")

        img = cv2.imread(f"assets/{img_name}", 0)
        (img_height, img_width) = img.shape[:2]
        aspect_ratio = img_height / img_width
        new_width = 500
        new_height = int(new_width * aspect_ratio)
        img = cv2.resize(img, (new_width, new_height))

        cv2.imshow(f"{img_name}", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print(" "*20 + "Done!")
    print(f"Finished displaying files in folder: '{ASSETS_DIR}'.")
    return 0

