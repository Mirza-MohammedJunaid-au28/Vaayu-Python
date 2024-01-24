import cv2
import numpy as np
import servo
import pada_navigation as pd
global height
global width 

cap = cv2.VideoCapture(1)

colour_ranges = {"RED": [[170, 85, 110], [180, 255, 255], [0, 85, 110], [7, 255, 255]],
                 "BLUE": [[94, 80, 2], [126, 255, 255], [0, 0, 0], [0, 0, 0]],
                 "PURPLE": [[129, 80, 10], [150, 255, 255], [0, 0, 0], [0, 0, 0]],
                 "YELLOW": [[15, 40, 50], [40, 255, 255], [0, 0, 0], [0, 0, 0]],
                 "ORANGE": [[10, 100, 20], [25, 255, 255], [0, 0, 0], [0, 0, 0]]}

move_servo_x = 0
move_servo_y = 0
isCircleDetacted = False
isCircleDetacted_pa = False
isCircleAligned = False

def centre_grid(frame, h, w):
    cv2.line(frame, (3*w // 10, 0), (3*w // 10, h), (120, 0, 0), 3)
    cv2.line(frame, (3*w // 10, 3*h // 10), (w - 3*w // 10, 3*h // 10), (120, 0, 0), 3)
    cv2.line(frame, (w - 3*w // 10, 0), (w - 3*w // 10, h), (120, 0, 0), 3)
    cv2.line(frame, (3*w // 10, h - 3*h // 10), (w - 3*w // 10, h - 3*h // 10), (120, 0, 0), 3)
    return


def show_nav(cir_x, cir_y, width, height):
    global move_servo_x,move_servo_y,isCircleAligned

    if(cir_x >= width - 3*width // 10):
        print("left down right up (MOVE RIGHT)\n RIGHT BOX")
        move_servo_x = -30
        move_servo_y = 30
        isCircleAligned = False
           
    
    elif(cir_x <= 3*width//10):
        print("left up right down (MOVE LEFT) \n LEFT BOX")
        move_servo_x = 30
        move_servo_y = -30
        isCircleAligned = False
         

    elif(cir_y >= height - 3*height // 10 and cir_x >= 3*width // 10 and cir_x <= width - 3*width // 10):
        print("Both down (MOVE DOWN)\n BOTTOM BOX")
        move_servo_x = -30
        move_servo_y = -30
        isCircleAligned = False
         

    else:
        isCircleAligned = True
        print("circle aligned")

    return

def grid(col):
    global isCircleDetacted
    count = 0
    color = colour_ranges[col]
    low_coul_1 = np.array(color[0])
    high_coul_1 = np.array(color[1])
    low_coul_2 = np.array(color[2])
    high_coul_2 = np.array(color[3])
    while True:
        key = cv2.waitKey(1)
        _, frame = cap.read()
        count += 1

        height = frame.shape[0]
        width = frame.shape[1]
        HSV_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        coul_mask_1 = cv2.inRange(HSV_frame, low_coul_1, high_coul_1)
        coul_mask_2 = cv2.inRange(HSV_frame, low_coul_2, high_coul_2)

        full_coul_mask = coul_mask_2 + coul_mask_1
        kernel = np.ones((10, 10), np.uint8)
        full_coul_mask = cv2.erode(full_coul_mask, kernel)
        full_coul_mask = cv2.medianBlur(full_coul_mask, 3)
        frame_gaussian = cv2.GaussianBlur(full_coul_mask, (5, 5), 2, 2)
        circles = cv2.HoughCircles(frame_gaussian, cv2.HOUGH_GRADIENT, 1, frame_gaussian.shape[0] / 8, param1=100, param2=18, minRadius=10, maxRadius=50)
        if circles is not None:
            circles = np.round(circles[0, :]).astype("int")
            cv2.circle(frame, center=(circles[0, 0], circles[0, 1]), radius=circles[0, 2], color=(0, 0, 0), thickness=2)
            cv2.line(frame, (circles[0, 0], circles[0, 1]), (width // 2, height // 2), (0, 255, 0), 3)
            show_nav(circles[0, 0], circles[0, 1], width, height)
            cv2.putText(frame, "Diameter : " + str((circles[0,2])*2), (0, 20), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
            isCircleDetacted = True
        else:
            isCircleDetacted = False
            
        if(count >= 30 and isCircleDetacted):
            if(not isCircleAligned):
                servo.move_servos(move_servo_x,move_servo_y)
                count = 0
            
        if(pd.reached_min_height):
            cv2.destroyWindow('frame')
            break

        cv2.imshow("Frame", frame)

        if key == 27:
            break
        
def pa_colour_det(col):
    global isCircleDetacted_pa
    color = colour_ranges[col]
    low_coul_1 = np.array(color[0])
    high_coul_1 = np.array(color[1])
    low_coul_2 = np.array(color[2])
    high_coul_2 = np.array(color[3])
    while True:
        key = cv2.waitKey(1)
        _, frame = cap.read()

        HSV_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        coul_mask_1 = cv2.inRange(HSV_frame, low_coul_1, high_coul_1)
        coul_mask_2 = cv2.inRange(HSV_frame, low_coul_2, high_coul_2)

        full_coul_mask = coul_mask_2 + coul_mask_1
        kernel = np.ones((10, 10), np.uint8)
        full_coul_mask = cv2.erode(full_coul_mask, kernel)
        full_coul_mask = cv2.medianBlur(full_coul_mask, 3)
        frame_gaussian = cv2.GaussianBlur(full_coul_mask, (5, 5), 2, 2)
        circles = cv2.HoughCircles(frame_gaussian, cv2.HOUGH_GRADIENT, 1, frame_gaussian.shape[0] / 8, param1=100, param2=18, minRadius=10, maxRadius=50)
        if circles is not None:
            circles = np.round(circles[0, :]).astype("int")
            cv2.circle(frame, center=(circles[0, 0], circles[0, 1]), radius=circles[0, 2], color=(0, 0, 0), thickness=2)
            isCircleDetacted_pa = True
            cv2.destroyAllWindows()
            break

        cv2.imshow("Frame", frame)
        
        if key == 27:
            break      

""" # grid()
print('1. Red \n2. Blue \n3. Green \n4. Yellow \n5. Orange')
ch = int(input('Enter : '))
keys = list(colour_ranges.keys())
grid(keys[ch - 1]) """