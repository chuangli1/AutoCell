from .sensors import ccs811,hdc1080

def genSensors():
    CO2,TVOC = ccs811.readCO2()
    TEMP, HUMI = hdc1080.readTemp()
    return [CO2,TVOC,TEMP,HUMI]


