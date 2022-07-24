import cv2
import numpy
import gaussian
import shape


src = cv2.imread('images/cat-blur.jpg', cv2.IMREAD_UNCHANGED)

hr_image = shape.resize(src)
mr_image = shape.resize(src, 600)

blurImage = gaussian.apply(hr_image, 10)

# Color balance
lut_in = [0, 255, 80]
lut_out = [0, 0, 255]

model = numpy.arange(0, 256)

lut_8u = numpy.interp(model, lut_in, lut_out).astype(numpy.uint8)
image_contrasted = cv2.LUT(blurImage, lut_8u)

result = shape.resize(image_contrasted, 600)

cv2.imshow('Unpixelate', numpy.hstack((mr_image, result)))
cv2.waitKey(0)
cv2.destroyAllWindows()
