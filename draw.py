import cv2 as cv
import numpy as np
import pickle
SIZE = 28

canvas = np.ones((SIZE * 4, SIZE * 4), dtype='uint8') * 255
canvas[
    int(SIZE/2) : ((SIZE*4)-int(SIZE/2)), 
    int(SIZE/2) : ((SIZE*4)-int(SIZE/2))
] = 0  # For drawing

start, end, is_drawing = None, None, False
def draw_line(image, start_point, end_point):
    cv.line(image, start_point, end_point, 255, 5)

def mouse_event(event, x, y, flags, params):
    global start, end, canvas, is_drawing
    # if event == cv.EVENT_LBUTTONDOWN and is_drawing: 
    if event == cv.EVENT_LBUTTONDOWN: 
        start = (x, y)
        is_drawing = True
    elif event == cv.EVENT_MOUSEMOVE and is_drawing:
        end = (x, y)
        start = end
        draw_line(canvas, start, end)
    elif event == cv.EVENT_LBUTTONUP: 
        is_drawing = False
        start = None
        end = None

cv.namedWindow("Test")
cv.setMouseCallback("Test", mouse_event)

pickle1 = np.array([])
pickled = 0

while(True):
    cv.imshow("Test", canvas)
    key = cv.waitKey(1) & 0xFF
    if key == ord('q'): break  # Quit
    elif key == ord('c'): 
        canvas = np.ones((SIZE * 4, SIZE * 4), dtype='uint8') * 255
        canvas[
            int(SIZE/2) : ((SIZE*4)-int(SIZE/2)), 
            int(SIZE/2) : ((SIZE*4)-int(SIZE/2))
        ] = 0
    elif key == ord('p'):  # Make a prediction
        image = canvas[
            int(SIZE/2) : ((SIZE*4)-int(SIZE/2)), 
            int(SIZE/2) : ((SIZE*4)-int(SIZE/2))
        ]
        print(image)
        print(image.shape)
        filename = 'Test_Pickles\\num.pkl'
        outfile = open(filename, 'wb')
        if pickled == 0: pickle1 = image
        if pickled == 1:
            pickle.dump(np.array([pickle1, image]), outfile)
            outfile.close()
            break
        pickled += 1

cv.destroyAllWindows()

# Tutorial for the code can be found here:
# https://medium.com/@edwardpie/building-a-cnn-for-recognising-mouse-drawn-digits-with-keras-opencv-mnist-72a7ae7a070a