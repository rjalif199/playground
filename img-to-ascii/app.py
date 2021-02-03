#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image
import click
import os.path


@click.command()
@click.argument('file')
@click.option('-w', '--max-width', type=int, default=80, show_default=True, help='Limit given image width with')
@click.option('-s', '--char-set', default='@&#%:*~=-.', show_default=True, help='Char set to use for converting')
@click.option('-f', '--factor', default=2, show_default=True, help='Squash height by this factor to make output look more natural')
def main(file, max_width, char_set, factor):
    """Converts graphics FILE into ASCII and prints into stdout."""

    with open(file, mode='rb') as f:
        image = Image.open(f).convert('L')
        src_w = image.width
        if src_w > max_width:
            ratio = src_w / image.height * factor
            image = image.resize((max_width, int(max_width / ratio)))

        cs_sz = len(char_set)
        max_val = 255
        data = tuple(int(val / max_val * (cs_sz - 1)) for val in image.getdata())

        s = ''
        for y in range(image.height):
            for x in range(image.width):
                s += char_set[data[image.width * y + x]]
            print(s)
            s = ''


if __name__ == '__main__':
    main()


