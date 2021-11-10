import pygame as pg


class CommonFuncs:

    @staticmethod
    def change_size(image, multiplier):
        img_size = image.get_size()
        return pg.transform.scale(image, (img_size[0] * multiplier, img_size[1] * multiplier))

    @staticmethod
    def set_size(image, x, y):

        return pg.transform.scale(image, (x, y))
