from datetime import datetime,time,timedelta

class ShiftSlot:
    isPrevDay = False
    startTime = None
    endTime = None
    shiftName = "Day"

class ShiftManager:
    
    def __init__(self):
        self.timeFormat = "%H:%M:%S"
        self.dateFormat = "%d-%m-%Y %H:%M:%S"
        self.shiftDict = {}
        self.slots = []
        
    def GetShiftSlots(self):
        # 12:00 AM - 08:30 AM (Prev-Day Night Shift-3),
        # 08:31 AM - 06:30 PM (Day Shift-1),
        # 06:31 PM - 10:30 PM (Second Shift-2),
        # 10:31 PM - 11:59 PM (Night Shift-3)
    
        slots = []
    
        slot = ShiftSlot()
    
        slot.isPrevDay = True
        slot.startTime = datetime.strptime("00:00:00",self.timeFormat).time()
        slot.endTime = datetime.strptime("08:30:00",self.timeFormat).time()
        slot.shiftName = "3"        
        slots.append(slot)
        
        slot = ShiftSlot()
    
        slot.isPrevDay = False
        slot.startTime = datetime.strptime("08:31:00",self.timeFormat).time()
        slot.endTime = datetime.strptime("18:30:00",self.timeFormat).time()
        slot.shiftName = "1"        
        slots.append(slot)
        
        slot = ShiftSlot()
    
        slot.isPrevDay = False
        slot.startTime = datetime.strptime("18:31:00",self.timeFormat).time()
        slot.endTime = datetime.strptime("22:30:00",self.timeFormat).time()
        slot.shiftName = "2"        
        slots.append(slot)
        
        
        slot = ShiftSlot()
    
        slot.isPrevDay = False
        slot.startTime = datetime.strptime("22:31:00",self.timeFormat).time()
        slot.endTime = datetime.strptime("23:59:00",self.timeFormat).time()
        slot.shiftName = "3"        
        slots.append(slot)
        
        return slots
        
    def addShift(self,key,value):
        if key in self.shiftDict:
            curValue = self.shiftDict.get(key)
            if value not in curValue:
                self.shiftDict[key] = curValue + "," + value
        else:
            self.shiftDict[key] = value 
                
    
    def printShift(self):
        for key, value in sorted(self.shiftDict.items()):
            print(key + ":" + value.replace("1","Day").replace("2","Second").replace("3","Night"))
            
            
    def GetShiftByDate(self, startDateTime,endDateTime):
        
        idxDateTimeValue = datetime.strptime(startDateTime,self.dateFormat)
        idxEndDateTimeValue = datetime.strptime(endDateTime,self.dateFormat)
        self.slots = self.GetShiftSlots()
        
        while idxDateTimeValue <= idxEndDateTimeValue:
            
            for idx in range(len(self.slots)):
                slot = self.slots[idx]                
                idxTimeValue = idxDateTimeValue.time()
                
                if idxTimeValue >= slot.startTime and idxTimeValue <= slot.endTime:
                    
                    shiftDate =  (idxDateTimeValue - timedelta(days=1)) if slot.isPrevDay else (idxDateTimeValue)
                    shiftDate = shiftDate.strftime('%d-%m-%Y')
                    shift = slot.shiftName
                    self.addShift(shiftDate, shift)
                    
                    if idxDateTimeValue == idxEndDateTimeValue:
                        idxDateTimeValue = idxDateTimeValue + timedelta(minutes=1)
                        break
                    
                    curDate = datetime.combine(idxDateTimeValue.date(),slot.endTime)
                    idxDateTimeValue = curDate + timedelta(minutes=1)
                    
                    if idxDateTimeValue > idxEndDateTimeValue:
                        idxDateTimeValue = idxEndDateTimeValue

        return self.shiftDict
                

x = ShiftManager()
x.GetShiftByDate("12-12-2019 01:01:00","15-12-2019 22:1:00")
x.printShift()
