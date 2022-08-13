import cv2
import numpy
import shape
import depixelate

src = cv2.imread('assets/cat.jpg', cv2.IMREAD_UNCHANGED)
mr_image = shape.resize(src, 600)

result = depixelate.apply(src, 8, 600)

cv2.imshow('Depixelate Preview', numpy.hstack((mr_image, result)))
cv2.waitKey(0)
cv2.destroyAllWindows()
