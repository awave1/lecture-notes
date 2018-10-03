#!/usr/bin/env python3

import os
from os import path
from os import environ as env
import glob
import argparse
import shutil as sh


parser = argparse.ArgumentParser()
parser.add_argument('course', type=str, nargs=1, help='course number')
parser.add_argument('lec', type=str, nargs=1, help='lecture number')
args = parser.parse_args()


def main():
    home = env.get('HOME')
    base_dir = env.get('SCREENSHOT_ROOT', home + '/Pictures/screenshots/')
    courses = ['cpsc418', 'cpsc471', 'grst205']
    courses_img = map(lambda x: os.getcwd() + '/' + x + '/img', courses)
    to = list(filter(lambda x: args.course[0] in x, courses_img))

    img_to = list(filter(lambda x: args.course[0] in x, courses))[0]

    if len(to) != 0:
        files = list(filter(path.isfile, glob.glob(base_dir + '*')))
        files.sort(key=lambda x: path.getmtime(x), reverse=True)
        lec = 'lec' + args.lec[0]

        to_dir = to[0] + '/' + lec
        src_file = files[0]
        if not path.exists(to_dir):
            os.makedirs(to_dir)

        imgs = sorted(os.listdir(to_dir), reverse=True)
        img_name = '0{}.png'.format(len(imgs) + 1)
        to_file = '{}/{}'.format(to_dir, img_name)

        img_path = '{}/img/{}/{}'.format(img_to, lec, img_name)

        sh.copy(src_file, to_file)
        os.system('echo "![{}]({})" | pbcopy'.format(img_name, img_path))


if __name__ == '__main__':
    main()
