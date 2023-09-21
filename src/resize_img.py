#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os.path import sep, isdir, isfile
from os import listdir
from pathlib import Path
from sys import argv, exit
from PIL import Image
import fnmatch

HELP = """
Script to resize images to 1000px height, from folder or one file, support PNG, JPEG

HOW TO USE:

    rsize image.png
    rsize .
    rsize /home/user/Pictures 
    
If you want to change something, you have to modify the script

"""


def get_path_abs(path_raw: str):
    path_file = Path(path_raw) or Path(".")

    if not path_file.is_absolute():
        return path_file.absolute()

    return path_file


def get_name(full_path: str) -> dict:
    """
    """
    name = full_path.split(sep)[-1]
    return {"name": name.split(".")[0],
            "extension": name.split(".")[-1]}

def search_type(name_file:str)-> bool:

    extensions = ["png", "jpeg", "jpg"]

    for ext in extensions:
        if fnmatch.fnmatch(name_file, f"*.{ext}"):
            return True
    return False

def read_files_from_folder(path):
    dir_list = listdir(path)

    for file in dir_list:
        if search_type(file):
            rsize(file)


def rsize(path: str, height_base=1000):
    path_img = get_path_abs(path)
    img = Image.open(path_img)

    if img.height > height_base:
        factor = height_base / img.height

        new_height = int(img.height * factor)
        new_width = int(img.width * factor)

        img_resize = img.resize((new_width, new_height))
        new_name = f'{get_name(path)["name"]}_r.{get_name(path)["extension"]}'
        img_resize.save(new_name)
        print(f"Factor: {factor}")
        print(f'File saved: {get_path_abs(new_name)}')
        return img_resize
    return img


def cli():
    if len(argv) < 2 or len(argv) > 2:
        print(HELP)
        exit(1)

    path_file = argv[1]

    if path_file == "--help":
        print(HELP)
        exit(0)

    try:
        if isdir(path_file):
            read_files_from_folder(path_file)
        else:
            rsize(path_file)
    except Exception as e:
        print(e)
        print(HELP)
        exit(1)

    exit(0)


def main():
    cli()


if __name__ == '__main__':
    main()
