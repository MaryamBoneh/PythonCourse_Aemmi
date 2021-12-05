import cv2, glob, random, argparse
from PIL import Image


class Snow:
    def __init__(self):
        self.x = random.randint(0, image.shape[1])
        self.y = random.randint(-800, image.shape[0])
        self.width = random.randint(4, 8)
        self.direction = random.choice([10, 8, 6, 4, 2, 0, -2, -4, -6, -8, -10])
        self.speed = random.choice([15, 20, 25, 30])

    def move(self):
        self.y += self.speed
        self.x += self.direction


image = cv2.imread('snow/img/Snow.jpeg', cv2.IMREAD_COLOR)
image_temp = image.copy()
row, col, _ = image.shape
snow_list = []
c = 10

for _ in range(200):
  snow_list.append(Snow())

for j in range(40):
  for i, s in enumerate(snow_list):
    s.move()
  image = image_temp.copy()
  for a in snow_list:
    cv2.circle(image, (int(a.x), a.y), a.width, (240, 240, 240), -1)
  c += 1
  cv2.imwrite(f'snow/img/shots/{c}.png', image)


imgs = glob.glob(f'snow/img/shots/*.png')
imgs.sort()
frames = []
for i in imgs:
    new_frame = Image.open(i)
    frames.append(new_frame)

frames[0].save(f'snow/img/shots/png_to_gif.gif', format='GIF',
               append_images=frames[1:],
               save_all=True,
               duration=250, loop=0)