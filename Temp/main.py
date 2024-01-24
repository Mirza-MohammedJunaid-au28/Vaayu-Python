#import gps
import math
#import sensor as se
from math import sin, cos, sqrt, atan2, radians
#import checkpoints as cp


#print('Coords1 : ',coords1)
xf_lat = 19.044092747384763
xf_log = 72.82096448939905

#4.532785845669279e-05

def startNavigation():
    coords1 = [19.043984992610433, 72.8209604660855]
    x1 = float(coords1[0])
    y1 = float(coords1[1])
    coords2 = [19.044056617850575, 72.82089743417322]
    x2 = float(coords2[0])
    y2 = float(coords2[1])
    slope_of_normal = (x1-x2) / (y2-y1)
    print('son : ',slope_of_normal)
    if slope_of_normal >= 0:
        x3 = (0.005 * math.cos(slope_of_normal)) + x2
        y3 = (0.005 * math.sin(slope_of_normal)) + y2
        x4 = (0.005 * math.cos(slope_of_normal)) - x2
        y4 = (0.005 * math.sin(slope_of_normal)) - y2        
    else:
        slope_of_normal = 180 - slope_of_normal
        x3 = (0.005 * math.cos(slope_of_normal)) + x2
        y3 = (0.005 * math.sin(slope_of_normal)) + y2
        x4 = (0.005 * math.cos(slope_of_normal)) - x2
        y4 = (0.005 * math.sin(slope_of_normal)) - y2
        """
        dist1 = math.sqrt(math.pow(x3-xf_lat,2) + math.pow(y3-xf_log,2))
        dist2 = math.sqrt(math.pow(x4-xf_lat,2) + math.pow(y4-xf_log,2))
        """
    dist1 = findDistance(x3,y3,xf_lat,xf_log)
    dist2 = findDistance(x4,y4,xf_lat,xf_log)
        
    print('dist1 : ',dist1 , '\n' , 'dist2 : ',dist2)
        
    if dist1 > dist2:
        print('Move Left')
            
    elif dist2 > dist1:
        print('Move Right')
    else:
        print('Move Straight')


def findDistance(sl1,sl2,dl1,dl2):
    R = 6371.0
    lat1 = radians(sl1)
    lon1 = radians(sl2)
    lat2 = radians(dl1)
    lon2 = radians(dl2)
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c * 1000
    return distance

startNavigation()