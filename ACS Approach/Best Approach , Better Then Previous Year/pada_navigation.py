import time
import sensor as se
import servo

deg1 = 0
deg2 = 0
reached_min_height = False

def navigations(checkpoints):
    global deg1, deg2, reached_min_height
    count = 0
    while True:
        pada_altitude = se.read_bmp388()
        checkpoint_altitude = checkpoints[count]

        if pada_altitude > 6:
            dist = abs(pada_altitude - checkpoint_altitude)
            if pada_altitude > checkpoint_altitude:
                print(f'Move Down {dist} Meters')
                count += 1
                """
                deg1 = 0
                deg2 = 0
                servo.move_servos(deg1,deg2)
                """
            elif pada_altitude < checkpoint_altitude:
                print('PADA is below the Checkpoint Altitude')
                if(dist <= 1):
                    print(f'Hold For Now {dist} Meters')
                else:
                    print(f'Move Up {dist} Meters')
                count += 1
                """
                deg1 = 0
                deg2 = 0
                servo.move_servos(deg1,deg2)
                """
            elif pada_altitude == checkpoint_altitude:
                print('Good go to Next Checkpoint')
                count += 1
        else:
            reached_min_height = True
            print('Propulsion Stop')
            break
        time.sleep(1)
    return           