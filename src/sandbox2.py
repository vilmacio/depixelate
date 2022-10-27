from PIL import Image
# from sandbox import get_energy_map

def matrix():
    img = Image.open('assets/chart-low.jpg')
    img = img.convert('RGBA')
    width, height = img.size
    # print(width)
    # print(height)

    over_img = Image.new('RGBA', (width * 10, height * 10))
    over_img_map = over_img.load()

    # for i in range(width):
    #     for j in range(height):
    #         img_map[i, j] = (220, 100, 25)

    for i in range(width * 10):
        for j in range(height * 10):
            if (j % 10 == 0 or i % 10 == 0):
                over_img_map[i, j] = (255, 255, 255, 255)
            else:
                over_img_map[i, j] = (0, 0, 0, 0)
            # if (j - i == 10 or j - i == 20 or j - i == 30 or j - i == 40):
            #     over_img_map[i, j - 10] = (255, 255, 255, 255)
            if ((j - i) % 10 == 0):
                over_img_map[i, j - 10] = (255, 255, 255, 100)

    img = img.resize((width * 10, height * 10), resample=0)
    new_img = Image.blend(img, over_img, 0.2)
    # return new_img
    new_img.show()

matrix()
