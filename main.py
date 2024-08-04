from features import display_images, camera, object_detector
from settings import ASSETS_DIR, MODELS_DIR


# display_images(ASSETS_DIR)

# camera()

object_detector(haarcascade_filepath="{MODELS_DIR}/haarcascade_frontalface_default.xml")
