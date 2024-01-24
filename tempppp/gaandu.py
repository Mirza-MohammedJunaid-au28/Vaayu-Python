"""
#import gps
import math
from math import radians, sin, atan2, sqrt, cos, degrees
#import sensor as se
import time
#import checkpoints as cp

# print('Coords1 : ',coords1)
"""
"""
xf_lat = 19.095305373477302
xf_log = 72.86043224909747


# 4.532785845669279e-05

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

def startNavigation():
    x1 = 19.08865730991935
    y1 = 72.86724138127246
    x2 = 19.08969418144148
    y2 = 72.86411111671808
    slope_of_normal = (x1 - x2) / (y2 - y1)
    theta = math.atan(slope_of_normal)
    print('son : ', slope_of_normal)
    print('theta : ', degrees(theta))
    if slope_of_normal >= 0:
        # right
        x3 = (0.00004532785845669279 * math.cos(math.radians(theta))) + x2
        y3 = (0.00004532785845669279 * math.sin(math.radians(theta))) + y2

        # left
        x4 = (0.00004532785845669279 * math.cos(math.radians(theta))) - x2
        y4 = (0.00004532785845669279 * math.sin(math.radians(theta))) - y2

    else:
        slope_of_normal = 180 - slope_of_normal
        # right
        x3 = (0.00004532785845669279 * math.cos(math.radians(theta))) + x2
        y3 = (0.00004532785845669279 * math.sin(math.radians(theta))) + y2

        # left
        x4 = (0.00004532785845669279 * math.cos(math.radians(theta))) - x2
        y4 = (0.00004532785845669279 * math.sin(math.radians(theta))) - y2
    
        dist1 = math.sqrt(math.pow(x3-xf_lat,2) + math.pow(y3-xf_log,2))
        dist2 = math.sqrt(math.pow(x4-xf_lat,2) + math.pow(y4-xf_log,2))
        
    dist1 = findDistance(x3, y3, xf_lat, xf_log)
    dist2 = findDistance(x4, y4, xf_lat, xf_log)

    # print('dist1 : ',dist1 , '\n' , 'dist2 : ',dist2)

    if dist1 > dist2:
        print('Move Left')
        # altitude = se.read_bmp388()

    elif dist2 > dist1:
        print('Move Right')
    
    else:
        print('Move Straight')

        # y = (((x2-x1)/(y2-y1)) * (x-x1)) + y1
        # print(coords1,coords2)

startNavigation()
"""

#import gps
import math
from  math import radians,sin,atan2,sqrt,cos,degrees
#import sensor as se
import time
#import checkpoints as cp

def findDistance(sl1,sl2,dl1,dl2):
    R = 6371.0
    lat1 = radians(sl1)
    lon1 = radians(sl2)
    lat2 = radians(dl1)
    lon2 = radians(dl2)
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)*2 + cos(lat1) * cos(lat2) * sin(dlon / 2)*2
    print('sqrt(a) : ',sqrt(a))
    print('sqrt(1-a) : ',sqrt(1-a))
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    print('c : ',c)
    distance = R * c * 1000
    return distance

# print('Coords1 : ',coords1)
xf_lat = 25.308558861899762
xf_log = 23.962693656574523


# 4.532785845669279e-05
"""
def startNavigation():
    coords1 = gps.giveMeCoords()
    while True:
        x1 = float(coords1[0])
        y1 = float(coords1[1])
        print('Sleep for 1 min')
        time.sleep(3)
        coords2 = gps.giveMeCoords()
        if (coords1 == coords2):
            print('Coordinates are Same , Sleeping for 3 sec')
            time.sleep(3)
            coords2 = gps.giveMeCoords()
        x2 = float(coords2[0])
        y2 = float(coords2[1])
        """
x2=21.997337032646506
y2=25.00248924893042
x1=23.24486936515781
y1=24.98008800800189
slope_of_normal = (x1 - x2) / (y2 - y1)
#theta = math.atan2((y1-y2),(x1-x2))
theta = math.atan(slope_of_normal)
print('son : ', slope_of_normal)
print('theta : ', degrees(theta))
time.sleep(1)

if theta >= 0:
    # right
    x3 = (0.00004532785845669279 * math.cos(math.radians(theta))) + x2
    y3 = (0.00004532785845669279 * math.sin(math.radians(theta))) + y2

    # left
    x4 = (0.00004532785845669279 * math.cos(math.radians(theta))) - x2
    y4 = (0.00004532785845669279 * math.sin(math.radians(theta))) - y2

else:
    theta = 180 - theta
    # right
    x3 = (0.00004532785845669279 * math.cos(math.radians(theta))) + x2
    y3 = (0.00004532785845669279 * math.sin(math.radians(theta))) + y2

    # left
    x4 = (0.00004532785845669279 * math.cos(math.radians(theta))) - x2
    y4 = (0.00004532785845669279 * math.sin(math.radians(theta))) - y2
"""
"""
"""
dist1 = math.sqrt(math.pow(x3-xf_lat,2) + math.pow(y3-xf_log,2))
dist2 = math.sqrt(math.pow(x4-xf_lat,2) + math.pow(y4-xf_log,2))
"""
dist1 = findDistance(x3, y3, xf_lat, xf_log)
dist2 = findDistance(x4, y4, xf_lat, xf_log)

# print('dist1 : ',dist1 , '\n' , 'dist2 : ',dist2)

if dist1 > dist2:
    print('Move Left')
    # altitude = se.read_bmp388()

elif dist2 > dist1:
    print('Move Right')
else:
    print('Move Straight')

# y = (((x2-x1)/(y2-y1)) * (x-x1)) + y1
# print(coords1,coords2)
