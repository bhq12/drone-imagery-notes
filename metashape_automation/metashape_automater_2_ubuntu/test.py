from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time
import sys
mouse = PyMouse()
keyboard = PyKeyboard()

CURRENT_PROJECT_NAME = sys.argv[1]
print(f"CURRENT PROJ: {CURRENT_PROJECT_NAME}")

################
################
##UI CONSTANTS##
################
################

# MENU BAR OPTIONS
FILE_BUTTON_X = 1950
FILE_BUTTON_Y = 50

WORKFLOW_BUTTON_X = 2125
WORKFLOW_BUTTON_Y = 60

# SUB_OPTIONS

FILE_EXPORT_BUTTON_X = 2025
FILE_EXPORT_BUTTON_Y = 300

FILE_EXPORT_MOSAIC_BUTTON_X = 2190
FILE_EXPORT_MOSAIC_BUTTON_Y = 390

FILE_SAVE_AS_BUTTON_X = 3140
FILE_SAVE_AS_BUTTON_Y = 720

# EXPORT MENU OPTIONS
SETUP_BOUNDARIES_X=2720
SETUP_BOUNDARIES_Y=480


X_0_BOX_X=2900
X_0_BOX_Y=480

X_1_BOX_X=3000
X_1_BOX_Y=480

Y_0_BOX_X=2900
Y_0_BOX_Y=510

Y_1_BOX_X=3000
Y_1_BOX_Y=510

EXPORT_OK_BUTTON_X=2930
EXPORT_OK_BUTTON_Y=970

########################
########################
##UI CONTROL FUNCTIONS##
########################
########################


def export_segment(segment_number, project_name, x_0, x_1, y_0, y_1, mouse, keyboard):
    mouse.click(FILE_BUTTON_X, FILE_BUTTON_Y, 1)
    time.sleep(0.2)
    mouse.click(FILE_EXPORT_BUTTON_X, FILE_EXPORT_BUTTON_Y, 1)
    time.sleep(0.2)
    mouse.click(FILE_EXPORT_MOSAIC_BUTTON_X, FILE_EXPORT_MOSAIC_BUTTON_Y, 1)
    time.sleep(0.2)
    keyboard.type_string(f'{project_name}_{str(segment_number)}')
    time.sleep(0.2)
    mouse.click(FILE_SAVE_AS_BUTTON_X, FILE_SAVE_AS_BUTTON_Y, 1)
    time.sleep(0.2)
    mouse.click(SETUP_BOUNDARIES_X, SETUP_BOUNDARIES_Y, 1)
    time.sleep(0.2)
    mouse.click(X_0_BOX_X, X_0_BOX_Y, 1)
    mouse.click(X_0_BOX_X, X_0_BOX_Y, 1) 
    mouse.click(X_0_BOX_X, X_0_BOX_Y, 1)
    time.sleep(0.2)
    keyboard.type_string(str(x_0))
    time.sleep(0.2)
    mouse.click(X_1_BOX_X, X_1_BOX_Y, 1)
    mouse.click(X_1_BOX_X, X_1_BOX_Y, 1) 
    mouse.click(X_1_BOX_X, X_1_BOX_Y, 1)
    time.sleep(0.2)
    keyboard.type_string(str(x_1))

    time.sleep(0.2)
    mouse.click(Y_0_BOX_X, Y_0_BOX_Y, 1)
    mouse.click(Y_0_BOX_X, Y_0_BOX_Y, 1) 
    mouse.click(Y_0_BOX_X, Y_0_BOX_Y, 1)
    time.sleep(0.2)
    keyboard.type_string(str(y_0))
    time.sleep(0.2)
    mouse.click(X_1_BOX_X, Y_1_BOX_Y, 1)
    mouse.click(X_1_BOX_X, Y_1_BOX_Y, 1) 
    mouse.click(X_1_BOX_X, Y_1_BOX_Y, 1)
    time.sleep(0.2)
    keyboard.type_string(str(y_1))
    time.sleep(0.2)

    mouse.click(EXPORT_OK_BUTTON_X, EXPORT_OK_BUTTON_Y, 1)
    time.sleep(1)





X_LOWER_BOUNDARY = 148.489879
X_UPPER_BOUNDARY = 148.501822
Y_LOWER_BOUNDARY = -23.447088
Y_UPPER_BOUNDARY = -23.415502

x = X_LOWER_BOUNDARY
x_segments = []
while x < X_UPPER_BOUNDARY:
    x_segments.append(x)
    x += (X_UPPER_BOUNDARY - X_LOWER_BOUNDARY) / 32
x_segments.append(X_UPPER_BOUNDARY)

y = Y_LOWER_BOUNDARY
y_segments = []
while y < Y_UPPER_BOUNDARY:
    y_segments.append(y)
    y += (Y_UPPER_BOUNDARY - Y_LOWER_BOUNDARY) / 32

segment_number = 1
for i in range(len(x_segments) - 1):
    x_0 = x_segments[i]
    x_1 = x_segments[i + 1]
    for j in range(len(y_segments) - 1):
        y_0 = y_segments[j]
        y_1 = y_segments[j+1]
        print(f'x_0: {x_0}, x_1: {x_1}, y_0: {y_0}, y_1: {y_1}')
        export_segment(segment_number, CURRENT_PROJECT_NAME, x_0, x_1, y_0, y_1, mouse, keyboard)
        segment_number += 1
        print(f'COMPLETED SEGMENT{str(segment_number)}')







