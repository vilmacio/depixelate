import cv2
import numpy
import shape
import unpixelate

src = cv2.imread('images/cat-blur.jpg', cv2.IMREAD_UNCHANGED)
mr_image = shape.resize(src, 600)

result = unpixelate.apply(src, 8, 600)

cv2.imshow('Unpixelate Preview', numpy.hstack((mr_image, result)))
cv2.waitKey(0)
cv2.destroyAllWindows()
