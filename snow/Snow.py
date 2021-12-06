import cv2, glob, random
from PIL import Image


class Snow:
    def __init__(self):
        self.x = random.randint(0, image.shape[1])
        self.y = random.randint(-800, image.shape[0])
        self.width = random.randint(3, 6)
        self.direction = random.choice([5, 4, 2, 0, -2, -4, -5])
        self.speed = random.choice([5, 7, 10, 13])

    def move(self):
        self.y += self.speed
        self.x += self.direction


image = cv2.imread('snow/img/Snow.jpeg', cv2.IMREAD_COLOR)
output_addres = 'snow/img/shots/'
image_temp = image.copy()
row, col, _ = image.shape

snow_list = []
c = 10

for _ in range(450):
    snow_list.append(Snow())

for j in range(89):
    for i, s in enumerate(snow_list):
        s.move()
    image = image_temp.copy()
    for a in snow_list:
        cv2.circle(image, (int(a.x), a.y), a.width, (240, 240, 240), -1)
    c += 1
    cv2.imwrite(f'{output_addres}{c}.png', image)

imgs = glob.glob(f'{output_addres}*.png')
imgs.sort()
frames = []

for i in imgs:
    new_frame = Image.open(i)
    frames.append(new_frame)

frames[0].save(f'{output_addres}png_to_gif.gif', format='GIF',
               append_images=frames[1:],
               save_all=True,
               duration=120, loop=0)