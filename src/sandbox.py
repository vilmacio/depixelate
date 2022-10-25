def scale(number, original_scale, new_scale):
    min_original, max_original = original_scale
    min, max = new_scale
    result = (max - min) * (number - min_original) / (max_original - min_original) + min

    return result

# test = scale(626, (0, 626), (0, 255))

from PIL import Image
from math import pow, sqrt
  
input_image = Image.open('assets/cat.jpg')
pixel_map = input_image.load()
width, height = input_image.size

energy_map = []

energy_image = Image.new('RGB', (width, height))
ei_pixel_map = energy_image.load()

ENERGY_SCALE = [0, 626]

for i in range(width):
    energy_map.append([])
    for j in range(height):

        if (j == 0 or i == 0 or i == (width - 1) or j == (height - 1)):
            energy_map[i].append(626)
        else:
            lR, lG, lB = input_image.getpixel((i - 1, j))
            mR, mG, mB = input_image.getpixel((i, j))
            rR, rG, rB = input_image.getpixel((i + 1, j))

            energy_sum = pow(lR - mR, 2) + pow(lG - mG, 2) + pow(lB - mB, 2) + pow(rR - mR, 2) + pow(rG - mG, 2) + pow(rB - mB, 2)
            energy = sqrt(energy_sum)

            energy_map[i].append(energy)
            
for i in range(width):
    for j in range(height):
        energy_value = energy_map[i][j]
        energy_pixel_color = round(scale(energy_value, ENERGY_SCALE, (0, 255)))
        ei_pixel_map[i, j] = (energy_pixel_color, energy_pixel_color, energy_pixel_color)

energy_image.show()
