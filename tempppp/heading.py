from math import atan2,pi

mx_sample=  []
my_sample=  []
mz_sample=  []
Mxyz = []
mx_center = 0
my_center = 0
mz_center = 0
mx_max = 0
my_max = 0
mz_max = 0
mx_min = 0
my_min = 0
mz_min = 0

def getHeading():
    heading = 180 * atan2(Mxyz[1],Mxyz[0]) / pi
    if(heading < 0) : heading += 360
    print(heading)

def getCompass_Data():
    global Mxyz
    # data reading
    pass

def get_one_sample_data_mxyz():
    global mx_sample,my_sample,mz_sample
    getCompass_Data()
    mx_sample[2] = Mxyz[0]
    my_sample[2] = Mxyz[1]
    mz_sample[2] = Mxyz[2]

def getCompassDate_calibrated():
    global Mxyz,mx_center,my_center,mz_center
    getCompass_Data()
    Mxyz[0] = Mxyz[0] - mx_center;
    Mxyz[1] = Mxyz[1] - my_center;
    Mxyz[2] = Mxyz[2] - mz_center;


def get_calibration_Data():
    global mx_sample,mx_max,my_max,mz_max,mx_min,my_min,mz_min,mx_center,my_center,mz_center
    for i in range(5000):
        get_one_sample_data_mxyz()

        if(mx_sample[2] >= mx_sample[1]) : mx_sample[1] = mx_sample[2]
        if(my_sample[2] >= my_sample[1]) : my_sample[1] = my_sample[2]
        if(mz_sample[2] >= mz_sample[1]) : mz_sample[1] = mz_sample[2]
        
        if(mx_sample[2] <= mx_sample[1]) : mx_sample[1] = mx_sample[2]
        if(my_sample[2] <= my_sample[1]) : my_sample[1] = my_sample[2]
        if(mz_sample[2] <= mz_sample[1]) : mz_sample[1] = mz_sample[2]

    mx_max = mx_sample[1]
    my_max = my_sample[1]
    mz_max = mz_sample[1]

    mx_min = mx_sample[0]
    my_min = my_sample[0]
    mz_min = mz_sample[0]

    mx_center = (mx_max + mx_min) / 2;
    my_center = (my_max + my_min) / 2;
    mz_center = (mz_max + mz_min) / 2;

def main():
    while True:
        getCompassDate_calibrated()
        getHeading()
        