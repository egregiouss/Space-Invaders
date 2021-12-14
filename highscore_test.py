import os
import shutil

import pytest
from game.highscore import Highscore


def clear_dir():
    for filename in os.listdir(os.getcwd()):
        file_path = os.path.join(os.getcwd(), filename)
        if 'data' in filename:
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))

def test_adding():
    h = Highscore()
    h.add("egor", 200)
    h.add("andrey", 400)
    h.add("alex", 1200)
    res = h.get_all()
    h.__del__()
    assert res == {"alex": 1200,
                   "andrey": 400,
                   "egor": 200}
    clear_dir()




def test_adding2_correct_order():
    h = Highscore()
    h.add("egor", 200)
    h.add("andrey", 400)
    h.add("alex", 1200)
    res = list(h.get_all().keys())
    h.__del__()
    assert res == ["alex",
                   "andrey",
                   "egor"]
    clear_dir()


def test_adding_incorrect_order():
    h = Highscore()
    h.add("egor", 200)
    h.add("andrey", 400)
    h.add("alex", 1200)
    res = list(h.get_all().keys())
    h.__del__()
    assert res != ["andrey",
                   "alex",
                   "egor"]
    clear_dir()


def test_adding_more_than_five_items():
    h = Highscore()
    h.add("egor", 200)
    h.add("andrey", 400)
    h.add("alex", 1200)
    h.add("A", 600)
    h.add("B", 500)
    h.add("C", 1300)
    res = list(h.get_all().keys())
    h.__del__()
    assert res == ["C",
                   "alex",
                   "A",
                   "B",
                   "andrey"]
    clear_dir()