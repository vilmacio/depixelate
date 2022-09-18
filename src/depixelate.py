import gaussian
import shape
import lut
import numpy
from PIL import Image
import cv2

def apply(image, weight = 6, output_scale = 800):

    pil_image = Image.open(image).convert('RGBA')

    width, height = pil_image.size
    
    image = numpy.array(pil_image)

    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    
    hr_image = shape.resize(image, (width, height))

    image_smothing = gaussian.apply(hr_image, weight)

    lut_result = lut.apply(image_smothing)

    result = shape.resize(lut_result, (width, height), output_scale)

    return result
