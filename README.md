# HomographyInImages
This python3 program places an image over another image pixel by pixel, by using homography.
## Requirement
- Python3
### Python Libraries Requirement
- matplotlib
- numpy
- cv2
- sklearn
## About Homography
Homography can map or project a pixel at point A to another point B, corresponding to its homography relation. Through this homographic relation, a whole image can be skewed, stretched, resized or translated. Homography is the relation of a pixel or collectively an image with itself, before and after its projection. This relation can be calculated using coordinates of pixels, atleast four pixels.
## Example
Initially two images are taken, one will act as a frame in which the other image will fit into. Four coordinates are taken as input by user as the outline of the frame and then image 2 is fit into image 1 and resultant image is saved in the same directory.
### Sample Run Input
./SampleImages/MyFrame.jpg
./SampleImages/Joker.jpg
187
153
343
175
185
461
343
432

### Frame
![Image 1 or Frame](SampleImages/MyFrame.jpg)
### Image to fit into frame
![Image 2 or Image to fit](https://github.com/muhammadmoiza/HomographyInImages/blob/master/SampleImages/Joker.jpg)
### Resultant image
![Resultant or Final Image](https://github.com/muhammadmoiza/HomographyInImages/blob/master/SampleImages/Image3.jpg)
