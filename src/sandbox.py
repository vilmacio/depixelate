def scale(number, original_scale, new_scale):
    min_original, max_original = original_scale
    min, max = new_scale
    result = (max - min) * (number - min_original) / (max_original - min_original) + min

    return result

# test = scale(626, (0, 626), (0, 255))

from PIL import Image
  
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
            lR = input_image.getpixel((i - 1, j))
            
for i in range(width):
    for j in range(height):
        energy_value = energy_map[i][j]
        energy_pixel_color = round(scale(energy_value, ENERGY_SCALE, (0, 255)))
        ei_pixel_map[i, j] = (energy_pixel_color, energy_pixel_color, energy_pixel_color)

energy_image.show()
