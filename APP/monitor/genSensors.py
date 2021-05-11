# from .sensors import ccs811,hdc1000
# from flask import json

# def genSensors():
#     while True:
#         try:
#             CO2,TVOC = ccs811.readCO2()
#             TEMP, HUMI = hdc1000.readTemp()
#             yield json.dumps({'sensors':[C02,TVOC,TEMP,HUMI]})
#         except:
#            break
from flask import json
def genSensors():
    while True:
        try:
            CO2,TVOC = [468,700]
            TEMP, HUMI = [28,30]
            yield json.dumps({'sensors': [CO2,TVOC,TEMP,HUMI]})
        except:
            print('s')
            break


