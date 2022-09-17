import cv2

def resize(image, original_size, width_scale = 1000):
    print(original_size)
    width, height = original_size

    ratio = width / height

    additional_width = width_scale - width

    additional_height = additional_width // ratio

    print(type(image))

    hr_image = cv2.resize(image, (int(width + additional_width), int(height + additional_height)))

    return hr_image