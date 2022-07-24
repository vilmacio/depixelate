import cv2
import numpy
import gaussian

src = cv2.imread('images/nike.jpg', cv2.IMREAD_UNCHANGED)

blurImage = gaussian.apply(src, 7)

# Color balance
lut_in = [0, 255, 80]
lut_out = [0, 0, 255]

model = numpy.arange(0, 256)

lut_8u = numpy.interp(model, lut_in, lut_out).astype(numpy.uint8)
image_contrasted = cv2.LUT(blurImage, lut_8u)

cv2.imshow('Gaussian Smoothing', numpy.hstack((src, image_contrasted)))
cv2.waitKey(0)
cv2.destroyAllWindows()
