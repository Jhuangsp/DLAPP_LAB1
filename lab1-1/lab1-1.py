import cv2
import numpy as np

def splitRGB(img):
    # TODO

    return R_map, G_map, B_map

def splitHSV(img):
    # TODO

    return H_map, S_map, V_map

def resize(img, size):
    # TODO

    return img_t

class MotionDetect(object):
    """docstring for MotionDetect"""
    def __init__(self, shape):
        super(MotionDetect, self).__init__()

        self.shape = shape
        self.avg_map = np.zeros((self.shape[0], self.shape[1]), dtype='float')
        self.alpha = 0.8 # you can ajust your value
        self.threshold = 40 # you can ajust your value

        print("MotionDetect init with shape {}".format(self.shape))

    def getMotion(self, img):
        assert img.shape == self.shape, "Input image shape must be {}, but get {}".format(self.shape, img.shape)

        # Extract motion part (hint: motion part mask = difference between image and avg > threshold)
        # TODO

        # Mask out unmotion part (hint: set the unmotion part to 0 with mask)
        # TODO

        # Update avg_map
        # TODO

        return motion_map


# ------------------ #
#     RGB & HSV      #
# ------------------ #
name = "../data.png"
img = cv2.imread(name)
if img is not None:
    print("Reading {} success. Image shape {}".format(name, img.shape))
else:
    print("Faild to read {}.".format(name))

R_map, G_map, B_map = splitRGB(img)
H_map, S_map, V_map = splitHSV(img)

cv2.imwrite('data_R.png', R_map)
cv2.imwrite('data_G.png', G_map)
cv2.imwrite('data_B.png', B_map)
cv2.imwrite('data_H.png', H_map)
cv2.imwrite('data_S.png', S_map)
cv2.imwrite('data_V.png', V_map)


# ------------------ #
#   Interpolation    #
# ------------------ #
name = "../data.png"
img = cv2.imread(name)
if img is not None:
    print("Reading {} success. Image shape {}".format(name, img.shape))
else:
    print("Faild to read {}.".format(name))

height, width, channel = img.shape
img_big = resize(img, 2)
img_small = resize(img, 0.5)
img_big_cv = cv2.resize(img, (width*2, height*2))
img_small_cv = cv2.resize(img, (width//2, height//2))

cv2.imwrite('data_2x.png', img_big)
cv2.imwrite('data_0.5x.png', img_small)
cv2.imwrite('data_2x_cv.png', img_big_cv)
cv2.imwrite('data_0.5x_cv.png', img_small_cv)

# ------------------ #
#  Video Read/Write  #
# ------------------ #
name = "../data.mp4"
# Input reader
cap = cv2.VideoCapture(name)
fps = cap.get(cv2.CAP_PROP_FPS)
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

# Output writer
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output1.avi', fourcc, fps, (w, h), True)

# Motion detector
mt = MotionDetect(shape=(h,w,3))

# Read video frame by frame
while True:
    # Get 1 frame
    success, frame = cap.read()

    if success:
        motion_map = mt.getMotion(frame)

        # Write 1 frame to output video
        out.write(motion_map)
    else:
        break

# Release resource
cap.release()
out.release()