import cv2, random, argparse
import numpy as np

my_parser = argparse.ArgumentParser()
my_parser.add_argument('--encrypted_image')
my_parser.add_argument('--key')
my_parser.add_argument('--output_path')
args = my_parser.parse_args()


def decrypt():
    decripted_image = cv2.imread(f'{args.encrypted_image}', cv2.IMREAD_GRAYSCALE)
    row, col = decripted_image.shape
    key = np.load(f'{args.key}')

    for k in range(row):
        for l in range(col):
            if (decripted_image[k, l] - key[k, l]) < 255:
                decripted_image[k, l] = decripted_image[k, l] - key[k, l] + 255
            else:
                decripted_image[k, l] = decripted_image[k, l] - key[k, l]

    cv2.imwrite(f'{args.output_path}/decripted_image.png', decripted_image)


decrypt()