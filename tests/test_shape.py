import unittest
import cv2
import src.shape

class TestSuite(unittest.TestCase):
    
    def test_dimensions(self):
        sut = src.shape.resize
        width_scale = 300

        img = cv2.imread('assets/cat.jpg')

        original_height, original_width, *_ = img.shape

        img_result = sut(img, width_scale)

        height, width, *_ = img_result.shape

        assert width == width_scale
        assert width != original_width
        assert height != original_height
