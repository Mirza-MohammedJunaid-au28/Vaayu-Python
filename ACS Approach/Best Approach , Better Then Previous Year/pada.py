from threading import Thread
import time 
import circle_detection as cd
import sensor as se
import distance_measurement as dm
import pada_navigation as pada_nav

def start_process_of_PADA(details):
    checkpoints = dm.giveMeCheckpoints(se.read_bmp388(),details[2],10)
    pada_nav.navigations(checkpoints)
    cd.grid()
    return