#!/usr/bin/env python3


import os
import glob
import argparse
import shutil as sh
from os import path
from os import environ as env
from PIL import Image


parser = argparse.ArgumentParser()
parser.add_argument('--action', type=str, metavar='action')
parser.add_argument('course', type=str, nargs=1, help='course number')
parser.add_argument('lec', type=str, nargs=1, help='lecture number')
args = parser.parse_args()


home = env.get('HOME')
base_dir = env.get('SCREENSHOT_ROOT', home + '/Pictures/screenshots/')
courses = ['cpsc418', 'cpsc471', 'grst205']
courses_img = map(lambda x: os.getcwd() + '/' + x + '/img', courses)


def resize_img(path, width=450):
    img = Image.open(path)
    (img_width, img_height) = img.size
    aspect_ratio = width / img_width
    height = int(img_height * aspect_ratio)
    img = img.resize((width, height), Image.ANTIALIAS)
    img.save(path)


def copy_screenshot():
    to = filter(lambda x: args.course[0] in x, courses_img)

    if len(to) != 0:
        files = filter(path.isfile, glob.glob(base_dir + '*'))
        files.sort(key=lambda x: path.getmtime(x), reverse=True)

        to_dir = to[0] + '/lec' + args.lec[0]
        src_file = files[0]
        if not path.exists(to_dir):
            os.makedirs(to_dir)

        imgs = sorted(os.listdir(to_dir), reverse=True)
        img_name = '0{}.png'.format(len(imgs) + 1)
        to_file = '{}/{}'.format(to_dir, img_name)

        sh.copy(src_file, to_file)


def resize_images():
    for course_img_dir in courses_img:
        for root, dirs, files in os.walk(course_img_dir):
            for file in files:
                if file.endswith('.png') or file.endswith('.jpg'):
                    resize_img(os.path.join(root, file))


def main():
    if args.action == 'scrot':
        copy_screenshot()
    elif args.action == 'resize_imaages':
        resize_images()


if __name__ == '__main__':
    main()
