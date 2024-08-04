import os
import numpy
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


def camera():
    capture = cv2.VideoCapture(0)

    while True:
        ret, frame = capture.read()
        width = int(capture.get(3))
        height = int(capture.get(4))

        image = numpy.zeros(frame.shape, numpy.uint8)
        smaller_frame = cv2.resize(frame, None, fx=0.5, fy=1)

        image[0:, :width // 2] = smaller_frame
        image[0:, width // 2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180)

        cv2.imshow("CameraOutput (press 'q' to exit)", image)

        if cv2.waitKey(1) in [ord("q"), ord("Q")]:
            break

    capture.release()
    cv2.destroyAllWindows()
    exit()


def object_detector(haarcascade_filepath: str, capture_file=0):
    haarcascade = haarcascade_filepath
    capture = cv2.VideoCapture(capture_file)
    capture.set(3, 640//2)  # w
    capture.set(4, 480//2)  # H

    while True:
        ret, frame = capture.read()

        face_cascade = cv2.CascadeClassifier(haarcascade)
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        face = face_cascade.detectMultiScale(frame_gray, 1.1, 4)

        for (x, y, w, h) in face:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0))

        cv2.imshow("ObjectDetector (press 'q' to exit)", frame)

        if cv2.waitKey(1) in [ord("q"), ord("Q")]:
            break

    capture.release()
    cv2.destroyAllWindows()
    exit()
