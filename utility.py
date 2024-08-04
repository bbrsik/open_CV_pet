import os


def is_folder_empty(folder: str):
    if len(os.listdir(folder)) == 0:
        return True
    else:
        return False


def should_rename_files_in_folder(folder: str):
    folder = folder
    filename_list = os.listdir(folder)
    if len(filename_list) == 0:
        return False

    for number, filename in enumerate(filename_list):
        if str(number) == filename[:len(str(number))]:
            continue
        else:
            return True
    return False


def rename_files_in_folder(folder: str):
    folder = folder
    filename_list = os.listdir(folder)

    for number, filename in enumerate(filename_list):
        source = f"{folder}/{filename}"
        extension = filename.split(".").pop()
        destination = f"{str(number)}.{extension}"
        os.rename(source, f"{folder}/{destination}")

    return 0


def resize_image(image):
    pass
