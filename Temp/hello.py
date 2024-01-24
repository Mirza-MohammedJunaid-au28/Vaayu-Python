from math import cos
lat = 19.04399513423922
lon = 72.82094303172678
Pi = 3.141592653
R=6378137

dn = 5
de = 3

dLat = dn/R
dLon = de/(R*cos(Pi*lat/180))

latO = lat + dLat * 180/Pi
lonO = lon + dLon * 180/Pi 

print(latO,lonO)