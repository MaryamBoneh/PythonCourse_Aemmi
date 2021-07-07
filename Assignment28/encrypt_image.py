import cv2, glob, random, argparse
from PIL import Image
import numpy as np

my_parser = argparse.ArgumentParser()
my_parser.add_argument('--image')
my_parser.add_argument('--output_path')
args = my_parser.parse_args()


def encrypt():
    image = cv2.imread(f'{args.image}', cv2.IMREAD_GRAYSCALE)
    row, col = image.shape
    key = np.zeros((row, col), dtype=int)
    encripted_image = np.zeros((row, col), dtype=int)

    for i in range(row):
        for j in range(col):
            key[i, j] = random.randint(0, 255)
    np.save(f'{args.output_path}/key.npy', key)

    for m in range(row):
        for n in range(col):
            if (image[m, n] + key[m, n]) > 255:
                encripted_image[m, n] = image[m, n] + key[m, n] - 255
            else:
                encripted_image[m, n] = image[m, n] + key[m, n]
    cv2.imwrite(f'{args.output_path}/encrypted_image.bmp', encripted_image)


encrypt()