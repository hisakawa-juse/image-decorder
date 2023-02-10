import sys
from PIL import Image
import pyocr
import glob
import itertools


class ImageDecorder:
    def __init__(self, args):
        self.__args = args
        engines = pyocr.get_available_tools()
        self.__engine = engines[0]

    def read(self):
        filenames = map(glob.glob, self.__args)
        self.__filenames = itertools.chain(*filenames)

    def write(self):
        for image in self.__filenames:
            txt = self.__engine.image_to_string(Image.open(image), lang="jpn")
            print(txt)

if __name__ == '__main__':
    decorder = ImageDecorder(sys.argv[1:])
    decorder.read()
    decorder.write()

# engines = pyocr.get_available_tools()
# engine = engines[0]

# filenames = map(glob.glob, sys.argv[1:])
# filenames = itertools.chain(*filenames)
# for image_file in filenames:
#     txt = engine.image_to_string(Image.open(image_file), lang="jpn")
#     print(txt)

