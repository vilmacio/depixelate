import io
import gaussian
import shape
import lut
import numpy
from PIL import Image
import cv2

def apply(image, weight = 6, output_scale = 800):
    _, buffer = cv2.imencode('.png', image)
    io_buf = io.BytesIO(buffer)

    pil_image = Image.open(io_buf).convert('RGBA')

    width, height = pil_image.size
    
    image = numpy.array(image)
    
    hr_image = shape.resize(image, (width, height))

    image_smothing = gaussian.apply(hr_image, weight)

    lut_result = lut.apply(image_smothing)

    result = shape.resize(lut_result, (width, height), output_scale)

    return result
