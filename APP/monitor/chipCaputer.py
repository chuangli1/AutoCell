from ..db.index import findLocations,findMonitorTasks
from stage import Sta

class moveToChip():
    def __init__(self,stage):
        self.stage = stage
        self.index = 0
    def moveNext(self,locationID,user):
        location = findLocations(locationID,user).split(',')
        angle = int(location[3])
        line = int(location[4])
        self.stage.changeLocation(line,angle)
        



    
