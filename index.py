import cv2
import numpy
import gaussian
import shape
import lut

src = cv2.imread('images/cat-blur.jpg', cv2.IMREAD_UNCHANGED)

hr_image = shape.resize(src)
mr_image = shape.resize(src, 600)

image_smothing = gaussian.apply(hr_image, 10)

# Color balance
lut_result = lut.apply(image_smothing)

result = shape.resize(lut_result, 600)

cv2.imshow('Unpixelate', numpy.hstack((mr_image, result)))
cv2.waitKey(0)
cv2.destroyAllWindows()
