from PIL import Image
from math import pow, sqrt
# from sandbox2 import matrix

def scale(number, original_scale, new_scale):
    min_original, max_original = original_scale
    min, max = new_scale
    result = (max - min) * (number - min_original) / \
        (max_original - min_original) + min

    return result

# test = scale(626, (0, 626), (0, 255))

def get_energy_map():
    input_image = Image.open('assets/chart-low.jpg')
    pixel_map = input_image.load()
    width, height = input_image.size

    energy_map = []

    energy_image = Image.new('RGB', (width * 10, height * 10))
    ei_pixel_map = energy_image.load()

    ENERGY_SCALE = [0, 626]

    for i in range(width):
        energy_map.append([])
        for j in range(height):

            # to do: handle different values to unpack
            if (i == 0):
                lR, lG, lB, *_ = input_image.getpixel((i, j))
                rR, rG, rB, *_ = input_image.getpixel((i + 1, j))
            elif (i == (width - 1)):
                lR, lG, lB, *_ = input_image.getpixel((i - 1, j))
                rR, rG, rB, *_ = input_image.getpixel((i, j))
            else:
                lR, lG, lB, *_ = input_image.getpixel((i - 1, j))
                rR, rG, rB, *_ = input_image.getpixel((i + 1, j))

            if (j == 0):
                bR, bG, bB, *_ = input_image.getpixel((i, j + 1))
                tR, tG, tB, *_ = input_image.getpixel((i, j))
            elif (j == (height - 1)):
                bR, bG, bB, *_ = input_image.getpixel((i, j))
                tR, tG, tB, *_ = input_image.getpixel((i, j - 1))
            else:
                bR, bG, bB, *_ = input_image.getpixel((i, j + 1))
                tR, tG, tB, *_ = input_image.getpixel((i, j - 1))

            mR, mG, mB, *_ = input_image.getpixel((i, j))

            energy_horizontal_sum = pow(lR - mR, 2) + pow(lG - mG, 2) + pow(lB - mB, 2) + \
                pow(rR - mR, 2) + pow(rG - mG, 2) + pow(rB - mB, 2)
            energy_horizontal = sqrt(energy_horizontal_sum)

            energy_vertical_sum = pow(bR - mR, 2) + pow(bG - mG, 2) + pow(bB - mB, 2) + \
                pow(tR - mR, 2) + pow(tG - mG, 2) + pow(tB - mB, 2)
            energy_vertical = sqrt(energy_vertical_sum)

            energy_map[i].append((energy_horizontal + energy_vertical) / 2)

    for i in range(width):
        for j in range(height):
            energy_value = energy_map[i][j]
            energy_pixel_color = round(scale(energy_value, ENERGY_SCALE, (0, 255)))
            ei_pixel_map[i, j] = (energy_pixel_color,
                                energy_pixel_color, energy_pixel_color)

    energy_image.show()
    # return energy_image

get_energy_map()
