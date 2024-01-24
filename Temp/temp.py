import math 
r_earth = 6378
latitude = 19.04409021197911
longitude = 72.82096381884678
pi = 3.141592653
dy = 3/1000
dx = 3/1000

"""
new_latitude  = latitude  + (dy / r_earth);
new_longitude = longitude + (dx / r_earth) / math.cos(latitude* 180/pi);

meters = 5
my_lat = 19.043992803019787
my_log = 72.8209436643346
coef = 5 / 111.32
new_lat = my_lat + coef
new_log = my_log + coef / math.cos(my_lat * 0.01745)
print(new_lat , new_log)
"""
new_latitude  = latitude  + (dy / r_earth) * (180 / pi);
new_longitude = longitude + (dx / (r_earth * math.cos(latitude * pi/180)) * (180 / pi) )
print(new_latitude , new_longitude)