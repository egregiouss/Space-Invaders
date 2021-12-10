import pygame as pg


class CommonFuncs:

    @staticmethod
    def change_size(image, multiplier):
        img_size = image.get_size()
        a = pg.transform.scale(image, (int(img_size[0] * multiplier), int(img_size[1] * multiplier)))

        return a

    @staticmethod
    def set_size(image, x, y):
        return pg.transform.scale(image, (x, y))
