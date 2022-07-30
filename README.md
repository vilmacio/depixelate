# Unpixelate
Resize and depixel low resolution images.

<img src="assets/main-preview.jpg" width="100%">

## Usage

```python
import cv2
import unpixelate

original_image = cv2.imread('image.jpg', cv2.IMREAD_UNCHANGED)

result = unpixelate.apply(original_image, 7, 600)
```

### Params
The **apply** method accepts 3 parameters:

- **Image (Required)**: Original image to be changed.
- **Weight (Optional)**: Indicates the power of the anti-aliasing algorithm. The higher the value, the more shape distortion. It must be between 1 and 10. Default value is 6.
- **Width Scale (Optional)**: Indicates the pixel scale of the output image. Default value is 800.
