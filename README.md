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
- **Weight (Optional)**: Indicates the power of the gaussian-blur algorithm. The higher the value, the more shape distortion. It must be between 1 and 10. Default value is 6.
- **Width Scale (Optional)**: Indicates the width of the output image. Default value is 800.

## Limitations
Unpixelate library helps with logos, graphics and some photographs, but it doesn't help when maximum sharpness and detail is needed.
In the majority of cases, you'll want to improve the quality of low resolution images (about 300 pixels wide or less). Otherwise you might be a little disappointed.

<div style="display: flex; justify-content: space-between">
<div style="display: block">
    <div>
    <img src="assets/smothing-enlargement.png" width="85%">
    </div>
    <mark>200 x 113</mark>.
    <mark>Smothing enlargement</mark>.
</div>
<div style="display: block">
    <div>
    <img src="assets/hard-edges-with-draw.png" width="85%">
    </div>
    <mark>200 x 113</mark>.
    <mark>Smothing enlargement</mark>.
</div>
</div>

## Plans

- [ ] Anti-aliasing
