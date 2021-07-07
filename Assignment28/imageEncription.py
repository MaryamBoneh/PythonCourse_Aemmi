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
    mask = np.zeros((row, col), dtype=int)
    encripted_image = np.zeros((row, col), dtype=int)

    for i in range(row):
        for j in range(col):
            mask[i, j] = random.randint(0, 255)
    np.save(f'{args.output_path}/mask.npy', mask)

    for m in range(row):
        for n in range(col):
            if (image[m, n] + mask[m, n]) > 255:
                encripted_image[m, n] = image[m, n] + mask[m, n] - 255
            else:
                encripted_image[m, n] = image[m, n] + mask[m, n]
    cv2.imwrite(f'{args.output_path}/encripted_image.bmp', encripted_image)


def decrypt():
    decripted_image = cv2.imread(f'{args.output_path}/encripted_image.bmp', cv2.IMREAD_GRAYSCALE)
    row, col = decripted_image.shape
    mask = np.load(f'{args.output_path}/mask.npy')

    for k in range(row):
        for l in range(col):
            if (decripted_image[k, l] - mask[k, l]) < 255:
                decripted_image[k, l] = decripted_image[k, l] - mask[k, l] + 255
            else:
                decripted_image[k, l] = decripted_image[k, l] - mask[k, l]

    cv2.imwrite(f'{args.output_path}/decripted_image.png', decripted_image)

encrypt()
decrypt()