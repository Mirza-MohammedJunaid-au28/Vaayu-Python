import pyfirmata
from tkinter import *

def left_move_servo(angle):
    pin9.write(angle)
def right_move_servo(angle):
    pin10.write(angle)
    
def main():
    global pin9,pin10
    
    board=pyfirmata.Arduino('COM6')

    iter8 = pyfirmata.util.Iterator(board)
    iter8.start()

    pin9 = board.get_pin('d:9:s')
    pin10 = board.get_pin('d:10:s')
    
    while True:
        angle = int(input('Enter :'))

        if angle == 0:
            left_angle,right_angle = map(int,input('Enter Degree : ').split())
            left_move_servo(left_angle)
            right_move_servo(right_angle)
        elif angle == 1:
           left_move_servo(90)
           right_move_servo(90)
        elif angle == 9:
            break
            return
        
    # move_servo(0)
    """
    root = Tk()
    scale = Scale(root, command = move_servo, to = 180, 
                  orient = HORIZONTAL, length = 400, label = 'Angle')
    scale.pack(anchor = CENTER)
    root.mainloop()
    """

main()