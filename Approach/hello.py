import checkpoint as cp
checkpoints = []
copied_checkpoint = []
def checkPath(checkpointss):
    global copied_checkpoint,checkpoints
    copied_checkpoint = checkpointss
    while True:
        plane_coordinates =  list(map(float,input("Enter Plane coordinates : ").split()))
        plane_altitude = float(input("Enter Altitude : "))
        curved_altitude = cp.findaltitude(plane_coordinates[0],plane_coordinates[1],destination_lat,destination_log)
        checkrange(plane_coordinates)
        print('Check Point Altitude is : ',curved_altitude)
        counter = 0

        for i in range(1,len(copied_checkpoint)):
            if (plane_coordinates[0] > checkpoints[i][0] and curved_altitude > plane_altitude):
                dist_log = abs(plane_coordinates[1] - checkpoints[i][1])
                dist_lat = abs(plane_coordinates[0] - checkpoints[i][0])
                dist_alt = abs(curved_altitude - plane_altitude) 
                if(dist_log > 6.56168):
                    print('New Route')
                    checkpoints = cp.create_checkpoint(plane_coordinates[0],plane_coordinates[1],destination_lat, destination_log, plane_length)
                    print(checkpoints)
                    checkPath(checkpoints) 
                print(f'Move {dist_log} in straight & {dist_lat} in Left & Up in {dist_alt}')
                checkpointss.pop(i)
                break

            # # If PADA is Right Side of Checkpoint & Down from Curved Altitude
            # if (plane_coordinates[0] == checkpoints[i][0] and curved_altitude > plane_altitude):
            #     dist_log = abs(plane_coordinates[1] - checkpoints[i][1])
            #     dist_lat = abs(plane_coordinates[0] - checkpoints[i][0])
            #     dist_alt = abs(curved_altitude - plane_altitude) 
            #     if(dist_log > 6.56168):
            #         print('New Route')
            #         checkpoints = cp.create_checkpoint(plane_coordinates[0],plane_coordinates[1],destination_lat, destination_log, plane_length)
            #         print(checkpoints)
            #         checkPath(checkpoints) 
            #     print(f'Move {dist_log} in straight & {dist_lat} in Left & Up in {dist_alt}')
            #     checkpointss.pop(i)
            #     break

            # If PADA is Right Side of Checkpoint & Up from Curved Altitude
            elif (plane_coordinates[0] > checkpoints[i][0] and curved_altitude < plane_altitude):
                dist_log = abs(plane_coordinates[1] - checkpoints[i][1])
                dist_lat = abs(plane_coordinates[0] - checkpoints[i][0]) 
                dist_alt = abs(curved_altitude - plane_altitude) 
                if(dist_log > 6.56168):
                    print('New Route')
                    checkpoints = cp.create_checkpoint(plane_coordinates[0],plane_coordinates[1],destination_lat, destination_log, plane_length)
                    print(checkpoints)
                    checkPath(checkpoints) 
                print(f'Move {dist_log} in straight & {dist_lat} in Left & Down in {dist_alt}')
                checkpointss.pop(i)
                break

            # If PADA is Left Side of Checkpoint & Down from Curved Altitude
            elif (plane_coordinates[0] < checkpointss[i][0] and curved_altitude > plane_altitude):
                dist_log = abs(plane_coordinates[1] - checkpointss[i][1]) 
                dist_lat = abs(plane_coordinates[0] - checkpointss[i][0]) 
                dist_alt = abs(curved_altitude - plane_altitude)    
                if(dist_log > 6.56168):
                    print('New Route')
                    checkpoints = cp.create_checkpoint(plane_coordinates[0],plane_coordinates[1],destination_lat, destination_log, plane_length)
                    print(checkpoints)
                    checkPath(checkpoints) 
                print(f'Move {dist_log} in straight & {dist_lat} in Right & Up in {dist_alt}')
                break

            # If PADA is Left Side of Checkpoint & Up from Curved Altitude
            elif (plane_coordinates[0] < checkpointss[i][0] and curved_altitude < plane_altitude):
                dist_log = abs(plane_coordinates[1] - checkpointss[i][1]) 
                dist_lat = abs(plane_coordinates[0] - checkpointss[i][0]) 
                dist_alt = abs(curved_altitude - plane_altitude)    
                if(dist_log > 6.56168):
                    print('New Route')
                    checkpoints = cp.create_checkpoint(plane_coordinates[0],plane_coordinates[1],destination_lat, destination_log, plane_length)
                    print(checkpoints)
                    checkPath(checkpoints) 
                print(f'Move {dist_log} in straight & {dist_lat} in Right & Down in {dist_alt}')
                break

            elif checkpointss[i][0] == plane_coordinates[0] and checkpointss[i][1] == plane_coordinates[1]:
                print(f'Crossed the Checkpoint{i} : {i}')
                checkpointss.pop(i)
                break
            
            
            

def checkrange(plane_coordinates):
    global checkpoints , copied_checkpoint
    counter = 0
    for i in checkpoints:
        if(i[1] >= plane_coordinates[1] and i[0] >= plane_coordinates[0]):
            print(f'Next Checkpoint is : Checkpoint{copied_checkpoint.index(i) + 1} , Coordinates {i[0],i[1]}')
            break
        counter += 1

source_lat = 0
source_log = 0
destination_lat = 200
destination_log = 200
""" source_lat = 21.99999826405264
source_log = 24.99999574717875
destination_lat = 22.000034324111308
destination_log = 25.002421134682407 """
plane_length = 2

checkpoints = cp.create_checkpoint(source_lat, source_log,destination_lat, destination_log, plane_length)
# curved_altitude = cp.findaltitude(source_lat,source_log,destination_lat,destination_log)
# print(checkpoints)
checkPath(checkpoints)