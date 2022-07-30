# Unpixelate
Resize and depixel low resolution images.

<img src="assets/main-preview.jpg" width="100%">

## Usage

```python
import cv2
import unpixelate

original_image = cv2.imread('image.jpg', cv2.IMREAD_UNCHANGED)

result = unpixelate.apply(original_image, 9, 600)
```
