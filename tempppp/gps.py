from math import atan2,cos,sin,radians,degrees

latitude2 = 69.15673956977766 
longitude2 = -44.41628755018999
latitude1 = 70.10655185613862
longitude1 = -25.175114636080895

"""

print(diff_long)
theta = atan2(sin(diff_long) * cos(latitude2), cos(latitude1) * sin(latitude2) - sin(latitude1) * cos(latitude2) * cos(diff_long))
print(theta)
print(sin(diff_long), cos(latitude2) , sin(diff_long) * cos(latitude2))
print(cos(latitude1), sin(latitude2),cos(latitude1) * sin(latitude2))
print(sin(latitude1),cos(latitude2),cos(diff_long),sin(latitude1) * cos(latitude2) * cos(diff_long))
print(cos(latitude1) * sin(latitude2) - sin(latitude1) * cos(latitude2) * cos(diff_long))
"""
"""
"""
diff_long = longitude2 - longitude1
#print(diff_long)
X = cos(radians(latitude2)) * sin(radians(diff_long))

Y = (cos(radians(latitude1)) * sin(radians(latitude2))) - (sin(radians(latitude1)) * cos(radians(latitude2)) * cos(radians(diff_long)))
#print(Y)

theta = atan2(X,Y)
print(degrees(theta))