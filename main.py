import cv2
import os
from settings import ASSETS_DIR
from utility import should_rename_files_in_folder, rename_files_in_folder

if should_rename_files_in_folder(ASSETS_DIR):
    rename_files_in_folder(ASSETS_DIR)
    print("renamed some files")

images = os.listdir(ASSETS_DIR)
if len(images) == 0:
    print("Notice:")
    print(f"'{ASSETS_DIR}' folder is empty!")
    print("/// SHUTTING DOWN ///")
    exit()

for img_name in images:
    print(img_name)

    img = cv2.imread(f"assets/{img_name}", 0)
    img = cv2.resize(img, (400, 400))

    cv2.imshow(f"{img_name}", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
