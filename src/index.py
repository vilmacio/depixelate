import cv2
import numpy
import src.gaussian as gaussian
import src.shape as shape
import src.lut as lut

src = cv2.imread('images/cat-blur.jpg', cv2.IMREAD_UNCHANGED)

hr_image = shape.resize(src)
mr_image = shape.resize(src, 600)

image_smothing = gaussian.apply(hr_image, 7)

lut_result = lut.apply(image_smothing)

result = shape.resize(lut_result, 600)

cv2.imshow('Unpixelate', numpy.hstack((mr_image, result)))
cv2.waitKey(0)
cv2.destroyAllWindows()
