#!/usr/bin/env python3

import glob
import os
from PIL import Image


def resize_img(path, width=450):
    img = Image.open(path)
    (img_width, img_height) = img.size
    aspect_ratio = width / img_width
    height = int(img_height * aspect_ratio)
    img = img.resize((width, height), Image.ANTIALIAS)
    img.save(path)


def main():
    courses = ['cpsc418', 'cpsc471', 'grst205']
    courses_img = map(lambda x: os.getcwd() + '/' + x + '/img', courses)
    for course_img_dir in courses_img:
        for root, dirs, files in os.walk(course_img_dir):
            for file in files:
                if file.endswith('.png') or file.endswith('.jpg'):
                    resize_img(os.path.join(root, file))


if __name__ == '__main__':
    main()
