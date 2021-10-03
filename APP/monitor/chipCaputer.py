from db.index import findLocations,findMonitorTasks

class moveToChip():
    def __init__(self,stage):
        self.stage = stage
        self.index = 0
    def moveNext(self,locationID,user):
        location = findLocations(locationID,user)
        print(location)
        angle = int(location[0][3])*360/100
        line = int(location[0][4])*200/100
        self.stage.changeLocation(line,angle)
        



    
