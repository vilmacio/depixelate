import cv2

def resize(image, width_scale = 1000):
    height, width, *_ = image.shape

    ratio = width / height

    additional_width = width_scale - width

    additional_height = additional_width // ratio

    hr_image = cv2.resize(image, (int(width + additional_width), int(height + additional_height)))

    return hr_image
