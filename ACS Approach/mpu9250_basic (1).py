import os
import sys
import time
import smbus
from imusensor.MPU9250 import MPU9250


def read_mpu9250():
	address = 0x68
	bus = smbus.SMBus(1)
	imu = MPU9250.MPU9250(bus, address)
	imu.begin()

	while True:
		imu.readSensor()
		imu.computeOrientation()

		print ("Accel x: {0} ; Accel y : {1} ; Accel z : {2}".format(round(imu.AccelVals[0]),round(imu.AccelVals[1]), round(imu.AccelVals[2])))
		print ("Gyro x: {0} ; Gyro y : {1} ; Gyro z : {2}".format(round(imu.GyroVals[0]),round( imu.GyroVals[1]), round(imu.GyroVals[2])))
		print ("Mag x: {0} ; Mag y : {1} ; Mag z : {2}".format(round(imu.MagVals[0]),round(imu.MagVals[1]), round(imu.MagVals[2])))
		print ("roll: {0} ; pitch : {1} ; yaw : {2}".format(round(imu.roll),round(imu.pitch),round(imu.yaw)))
		time.sleep(0.1)