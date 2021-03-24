import cv2 as cv
import numpy as np
from predict import predict
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
start = False
correct = 0
predicted = 0
outputs = ['\nPREDICTION | CORRECT | CUMULATIVE SCORE']

while(True):
    cv.imshow("Test", canvas)
    if start == False:
        start = True
        print('\n\nHow to use this app: Write out numbers in the pop-up windows. When you are done, use the \'p\' key to make a prediction. If it is correct, type \'Y\' in the console, otherwise type \'N\'. To clear the drawing area, press \'c\'. To end the program, press \'q\'.')
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
        p = int(predict(image))
        g = str(input(str(f'Was {str(p)} your number? ')))
        predicted += 1
        if 'y' in g.lower(): correct += 1
        score = '{:.2%}'.format(correct/predicted)
        output = '    ' + str(p) + '           ' + g.upper() + '          ' + score
        outputs.append(output)

cv.destroyAllWindows()
print('\n'.join(outputs))
print(f'\n\nFINAL SCORE: ' + '{:.2%}'.format(correct/predicted), end='\n\n')
