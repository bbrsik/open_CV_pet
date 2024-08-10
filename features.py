import os
import numpy
import cv2
from utility import should_rename_files_in_folder, rename_files_in_folder, is_folder_empty


def display_images(folder: str):
    if is_folder_empty(folder):
        print("Notice:")
        print(f"Folder '{folder}' is empty!")
        return -1

    if should_rename_files_in_folder(folder):
        rename_files_in_folder(folder)
        print(f"Finished renaming files in folder: '{folder}'.")

    images = os.listdir(folder)
    print(f"Displaying images in folder: '{folder}'.")
    for img_name in images:
        print("---------------------------")
        print(f"Displaying {img_name}...")

        img = cv2.imread(f"{folder}/{img_name}", 0)
        (img_height, img_width) = img.shape[:2]
        aspect_ratio = img_height / img_width
        new_width = 500
        new_height = int(new_width * aspect_ratio)
        img = cv2.resize(img, (new_width, new_height))

        cv2.imshow(f"{img_name}", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print(" "*20 + "Done!")
    print(f"Finished displaying files in folder: '{folder}'.")
    return 0


def camera():
    capture = cv2.VideoCapture(0)
    try:
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

    except AttributeError:
        print("Camera not found.")
        return -1

    finally:
        capture.release()
        cv2.destroyAllWindows()


def object_detector(haarcascade_filepath: str, capture_file=0):
    haarcascade = haarcascade_filepath
    capture = cv2.VideoCapture(capture_file)
    try:
        capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        capture.set(cv2.CAP_PROP_FPS, 30)

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

    except:
        print("Camera not found.")
        return -1

    finally:
        capture.release()
        cv2.destroyAllWindows()


def image_scanner(haarcascade_filepath: str, folder: str):
    if is_folder_empty(folder):
        print("Notice:")
        print(f"Folder '{folder}' is empty!")
        return -1

    if should_rename_files_in_folder(folder):
        rename_files_in_folder(folder)
        print(f"Finished renaming files in folder: '{folder}'.")

    haarcascade = haarcascade_filepath
    cascade = cv2.CascadeClassifier(haarcascade)
    images = os.listdir(folder)

    for img_name in images:
        img = cv2.imread(f"{folder}/{img_name}")
        if img is None:
            print(f"Error: Cannot load image '{img_name}'. Skipping.")
            continue

        (img_height, img_width) = img.shape[:2]
        aspect_ratio = img_height / img_width
        new_width = 500
        new_height = int(new_width * aspect_ratio)
        resized_img = cv2.resize(img, (new_width, new_height))

        img_gray = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)
        object_to_detect = cascade.detectMultiScale(img_gray, minSize=(30, 30))
        objects_amount = len(object_to_detect)

        print("---------------------------")
        print(f"Current image: {img_name}")
        print(f"Detected: {objects_amount}")

        if objects_amount != 0:
            for (x, y, w, h) in object_to_detect:
                cv2.rectangle(resized_img, (x, y),
                              (x + w, y + h),
                              (0, 255, 0))

        cv2.imshow(f"{img_name} (press 'q' to exit)", resized_img)
        print(" " * 20 + "Done!")
        print("---------------------------")
        if cv2.waitKey(0) in [ord("q"), ord("Q")]:
            print("////////////////////")
            print("Interrupted by user!")
            cv2.destroyAllWindows()
            break

        cv2.destroyAllWindows()
    print(f"Finished scanning files in folder: '{folder}'.")
    return 0
