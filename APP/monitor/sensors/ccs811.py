import time
import board
import busio
import adafruit_ccs811
 
i2c = busio.I2C(board.SCL, board.SDA)
ccs811 = adafruit_ccs811.CCS811(i2c)

def readCO2():
# Wait for the sensor to be ready
    try:
        if ccs811.data_ready:
            eco2 = ccs811.eco2
            tvoc = ccs811.tvoc
            print("CO2: {} PPM, TVOC: {} PPB".format(eco2, tvoc))
            return eco2, tvoc
    except:
        print('css811 Error!')


        