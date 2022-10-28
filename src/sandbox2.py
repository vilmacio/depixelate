from PIL import Image
from sandbox import get_energy_map

def matrix():
    img = get_energy_map()
    img = img.convert('RGBA')
    width, height = img.size
    # print(width)
    # print(height)

    SCALE = 2

    over_img = Image.new('RGBA', (width * SCALE, height * SCALE))
    over_img_map = over_img.load()

    # for i in range(width):
    #     for j in range(height):
    #         img_map[i, j] = (220, SCALE0, 25)

    for i in range(width * SCALE):
        for j in range(height * SCALE):
            if (j % SCALE == 0 or i % SCALE == 0):
                over_img_map[i, j] = (255, 255, 255, 255)
            else:
                over_img_map[i, j] = (0, 0, 0, 0)
            # if (j - i == SCALE or j - i == 20 or j - i == 30 or j - i == 40):
            #     over_img_map[i, j - SCALE] = (255, 255, 255, 255)
            if ((j - i) % SCALE == 0):
                over_img_map[i, j - SCALE] = (255, 255, 255, 100)

    img = img.resize((width * SCALE, height * SCALE), resample=0)
    new_img = Image.blend(img, over_img, 0.2)
    # return new_img
    new_img.show()

matrix()
