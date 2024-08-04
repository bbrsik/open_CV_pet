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

    for img_name in images:
        print(img_name)

        img = cv2.imread(f"assets/{img_name}", 0)
        img = cv2.resize(img, (400, 400))

        cv2.imshow(f"{img_name}", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return 0
