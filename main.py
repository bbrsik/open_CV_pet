from features import display_images, camera, object_detector, image_scanner
from settings import ASSETS_DIR, MODELS_DIR, VIDEOS_DIR


while True:
    print("------------------------")
    print("1. display_images")
    print("2. camera")
    print("3. object_detector")
    print("4. photo_scanner")
    print("0. exit")
    print("________________________")
    variant = str(input())
    match variant:
        case "1":
            display_images(ASSETS_DIR)
        case "2":
            camera()
        case "3":
            object_detector(haarcascade_filepath=f"{MODELS_DIR}/haarcascade_frontalface_default.xml",
                            capture_file=f"{VIDEOS_DIR}/Minion.mp4")
        case "4":
            image_scanner(haarcascade_filepath=f"{MODELS_DIR}/haarcascade_frontalface_default.xml",
                          folder=f"{ASSETS_DIR}/")
        case "0":
            print("Shutting down.")
            break
        case _:
            print("Bad input. Please try again.")
