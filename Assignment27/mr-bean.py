import cv2, random, argparse
import numpy as np

# my_parser = argparse.ArgumentParser()
# my_parser.add_argument('--image')
# my_parser.add_argument('--output_path')
# args = my_parser.parse_args()


def add_noise():
    image = cv2.imread('Assignment27/assets/img/mr_bean.jpeg', cv2.IMREAD_GRAYSCALE)
    row , col = image.shape
    for i in range(10000):
        y_coord=random.randint(0, row - 1)
        x_coord=random.randint(0, col - 1)
        image[y_coord:y_coord+1, x_coord:x_coord+1] = 255
    for i in range(10000):
        y_coord=random.randint(0, row - 1)
        x_coord=random.randint(0, col - 1)
        image[y_coord:y_coord+1, x_coord:x_coord+1] = 0
    cv2.imwrite(f'Assignment27/assets/img/mr_bean_sp_noise.png', image)


def destroy_noise():
    image = cv2.imread('Assignment27/assets/img/mr_bean_sp_noise.png', cv2.IMREAD_GRAYSCALE)
    row , col = image.shape
    for m in range(1, row - 1):
        for n in range(1, col - 1):
            small_image = image[m-1:m+2, n-1:n+2]
            sorted_numbers = np.sort(small_image, axis=None)
            image[m, n] = sorted_numbers[4]

    cv2.imwrite(f'Assignment27/assets/img/mr_bean_destroy_noise.png', image)

add_noise()
destroy_noise()