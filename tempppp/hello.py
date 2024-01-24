import math 
def getNewLatitude(latitude, distanceKm):
    meridionalRadiuskm = 40007.86;
    latitude = (latitude + distanceKm / (meridionalRadiuskm / 360));
    if (latitude > 90): return 180 - latitude;
    if (latitude < -90): return -(180 + latitude);
    return latitude;


print(getNewLatitude(19.043989528216134, 10));
#print(getNewLatitude(50, -100));

#  This function may also be useful, you can use this to get a new location base on a north/south / east/west offset in km. Note that accuracy will start to reduce as the offset increases. 
def getNewLocation(lat, lon, offsetNorthKm, offsetEastKm):
    ONE_DEGREE_KM = 111.32;

    deltaLatitude = offsetNorthKm / ONE_DEGREE_KM;
    deltaLongitude = offsetEastKm / (ONE_DEGREE_KM * math.cos(math.pi * lat / 180));

    result = { 
        lat:  lat + deltaLatitude,
        lon:  lon + deltaLongitude
    }
    return result;