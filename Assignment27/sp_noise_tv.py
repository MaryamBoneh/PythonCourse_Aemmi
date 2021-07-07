import cv2, glob, random, argparse
from PIL import Image

my_parser = argparse.ArgumentParser()
my_parser.add_argument('--image')
my_parser.add_argument('--output')
args = my_parser.parse_args()

def add_noise(c):
    image = cv2.imread(args.image, cv2.IMREAD_GRAYSCALE)
    screen = image[450:800, 480:950]
    row , col = screen.shape
    number_of_pixels_white = random.randint(3500, 5000)
    number_of_pixels_black = random.randint(3500, 5000)
    for i in range(number_of_pixels_white):
        y_coord=random.randint(0, row - 1)
        x_coord=random.randint(0, col - 1)
        screen[y_coord:y_coord+3, x_coord:x_coord+3] = 255
    for i in range(number_of_pixels_black):
        y_coord=random.randint(0, row - 1)
        x_coord=random.randint(0, col - 1)
        screen[y_coord:y_coord+3, x_coord:x_coord+3] = 0
    image[450:800, 480:950] = screen
    cv2.imwrite(f'{args.output}/screen{c}.png', image)

for _ in range(20):
  add_noise(_)
  
imgs = glob.glob(f'{args.output}/*.png')
frames = []
for i in imgs:
    new_frame = Image.open(i)
    frames.append(new_frame)

frames[0].save(f'{args.output}/png_to_gif.gif', format='GIF',
               append_images=frames[1:],
               save_all=True,
               duration=300, loop=0)