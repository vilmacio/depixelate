import cv2

def apply(image, weight = 5):
    ksizes = [1, 1]

    if (weight < 1 or weight > 10):
        raise Exception("Weight must be between 0 and 10. The received value was {}".format(weight))

    ksizes[0] = ksizes[1] = weight * 2

    if (ksizes[0] % 2 == 0):
        ksizes[0] = ksizes[1] = ksizes[1] - 1

    result = cv2.GaussianBlur(image, ksizes, cv2.BORDER_DEFAULT)

    return result
