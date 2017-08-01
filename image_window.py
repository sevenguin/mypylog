# -*- coding:utf-8 -*-
"""Mac OX安装dlib时，缺失类补足

使用如下方法安装：
brew install boost
brew install boost-python --with-python3 --without-python
conda install -c menpo dlib
虽然安装成功了，但是dlib.image_window类缺失，这个包就是提供这个类的相关方法
dlib.image_window相关介绍见：http://dlib.net/python/index.html#dlib.image_window
"""

import copy
from skimage import io


class image_window:
    def __init__(self):
        self.img = None
        self.origin_img = None

    def add_overlay(self, dets, rgb_pixel=(255, 0, 0)):
        for det in dets:
            r_0, r_1, c_0, c_1 = min(det.top(), det.bottom()), max(det.top(), det.bottom()), min(det.left(), det.right()), max(det.left(), det.right())
            self.img[r_0: r_1, c_0] = rgb_pixel
            self.img[r_0: r_1, c_1] = rgb_pixel
            self.img[r_0, c_0: c_1] = rgb_pixel
            self.img[r_1, c_0: c_1] = rgb_pixel
        self.show()

    def show(self):
        io.imshow(self.img)
        io.show()

    def set_image(self, img):
        self.origin_img = img
        self.img = img

    def clear_overlay(self):
        self.img = copy.deepcopy(self.origin_img)
