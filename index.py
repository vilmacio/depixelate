import cv2
import numpy

src = cv2.imread('images/cat-pixelate.png', cv2.IMREAD_UNCHANGED)

# Gaussian blur
blurImage1 = cv2.GaussianBlur(src, (7,7), cv2.BORDER_DEFAULT)
blurImage2 = cv2.GaussianBlur(blurImage1, (7,7), cv2.BORDER_DEFAULT)
blurImage3 = cv2.GaussianBlur(blurImage2, (7,7), cv2.BORDER_DEFAULT)
blurImage4 = cv2.GaussianBlur(blurImage3, (7,7), cv2.BORDER_DEFAULT)
blurImage = cv2.GaussianBlur(blurImage4, (7,7), cv2.BORDER_DEFAULT)

# Color balance
lut_in = [0, 255, 100]
lut_out = [0, 100, 255]

lut_8u = numpy.interp(numpy.arange(0, 256), lut_in, lut_out).astype(numpy.uint8)
image_contrasted = cv2.LUT(blurImage, lut_8u)

cv2.imshow('Gaussian Smoothing', numpy.hstack((src, blurImage, image_contrasted)))
cv2.waitKey(0)
cv2.destroyAllWindows()
