from math import cos,sin,atan,tan,pi,pow,e,log
"""
"""
s_lat = 0
s_log = 0
d_lat = 180
d_log = 180

if d_log - s_log <= 180:
    diff_log = d_log - s_log
elif d_log - s_log < -180:
    diff_log = 360 + d_log - s_log
elif d_log - s_log > 180:
    diff_log = d_log - s_log - 360

#theta = atan(diff_log / (tan((pi/4)+(d_lat/2) * )) - () )

a = tan((pi/4)+(d_lat/2))
b = pow(1-(e*sin(d_lat))/1+(e*sin(d_lat)),(e/2))
c = tan((pi/4)+(s_lat/2))
d = pow((1-(e*sin(s_lat)))/(1+(e*sin(s_lat))),e/2)

theta = atan(diff_log / (log(a*b)-  log(c*d)))
print(theta)