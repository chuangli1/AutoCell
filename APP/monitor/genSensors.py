from .sensors import ccs811,hdc1000

# def genSensors():
#     CO2,TVOC = ccs811.readCO2()
#     TEMP, HUMI = hdc1000.readTemp()
#     return [C02,TVOC,TEMP,HUMI]
test1 = 1
test = 0
def genSensors():
    CO2,TVOC = [test1+1,test]
    TEMP, HUMI = [test-0.1,test]
    return [C02,TVOC,TEMP,HUMI]


