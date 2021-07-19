import cv2
import numpy as np

video = cv2.VideoCapture(0)
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

def detectColor(center_square):
  black = 0
  white = 0
  gray = 0
  for i in range(center_square.shape[0]):
    for j in range(center_square.shape[1]):
      if center_square[i,j,0] <= 40:
        black += 1
      elif center_square[i,j,0] >= 230:
        white += 1
      else:
        gray += 1
    if black >= gray and black >= white:
      return 'black'
    elif white >= black and black >= gray:
      return 'white'
    else:
      return 'gray'

while True:

    validation, frame = video.read()
    if validation is not True:
        break

    roi = frame[int(height/2) -100: int(height/2) +100, int(width/2) -100: int(width/2) +100]

    color = detectColor(roi)

    blured_frame = cv2.blur(frame, (60, 60))
    blured_frame[int(height/2) -100: int(height/2) +100, int(width/2) -100: int(width/2) +100] = roi

    cv2.putText(blured_frame, "Color: {}".format(color), (50, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0), 2)
    cv2.imshow('output', blured_frame)
    cv2.waitKey(30)
