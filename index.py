import cv2
import numpy

src = cv2.imread('images/cat.png', cv2.IMREAD_UNCHANGED)

# Gaussian blur
# dst = cv2.GaussianBlur(src, (7,7), cv2.BORDER_DEFAULT)

# Color balance
lut_in = [0, 27, 255]
lut_out = [0, 0, 255]

lut_8u = numpy.interp(numpy.arange(0, 256), lut_in, lut_out).astype(numpy.uint8)
image_contrasted = cv2.LUT(src, lut_8u)

cv2.imshow('Gaussian Smoothing', numpy.hstack((src, image_contrasted)))
cv2.waitKey(0)
cv2.destroyAllWindows()
