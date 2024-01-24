import time
import board
import adafruit_bmp3xx
i2c = board.I2C()
bmp = adafruit_bmp3xx.BMP3XX_I2C(i2c)

bmp.sea_level_pressure = 1007.2
print('Altitude: {} meters'.format(bmp.altitude))
