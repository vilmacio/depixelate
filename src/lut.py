import cv2
import numpy

def apply(image):
    lut_in = [0, 255, 80]
    lut_out = [0, 0, 255]

    model = numpy.arange(0, 256)

    lut_8u = numpy.interp(model, lut_in, lut_out).astype(numpy.uint8)
    result = cv2.LUT(image, lut_8u)

    return result
