import cv2
import matplotlib.pyplot as plt 
import numpy as np

image = cv2.imread('Assignment29/assets/img/noisey_OCR.jpg', cv2.IMREAD_GRAYSCALE)

row , col = image.shape
for m in range(1, row - 1):
    for n in range(1, col - 1):
        small_image = image[m-1:m+2, n-1:n+2]
        sorted_numbers = np.sort(small_image, axis=None)
        image[m, n] = sorted_numbers[4]

_, thresh = cv2.threshold(image,110,255,cv2.THRESH_BINARY)

rows = []
for m in range(1, row - 1):
    find_top = False
    find_buttom = True
    if find_buttom:
        for n in range(col):
            if not find_top:
                if thresh[m, n] == 255:
                    rows.append(m)
                    find_top = True
            else:
                find_buttom = False
                break
    if not find_buttom:
        if thresh[m, 1:col-1].all():
            thresh[m, 0:col] = 40
            rows.append(m)
cv2.imwrite('Assignment29/assets/img/noisey_OCR_output.jpg', thresh)
print(rows)      