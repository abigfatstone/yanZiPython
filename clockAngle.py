# -*- coding: UTF-8 -*-

class ClockAngle:

    def getClockInput(self,inUserSaid):
        return ['calc_clock_angle',"请输入要计算的时间，以HH:MI:SS的格式,例如04:35:00"]

    def calcClockAngle(self,inTime):
        try:
            dTimeDetail = inTime.split(":")
   
            sHour = int(dTimeDetail[0])
            sMinute = int(dTimeDetail[1])
            sSecond = int(dTimeDetail[2])
            # 检查输入的数值
            if sHour > 12 and sHour <=23:
                sHour = sHour - 12
            if sHour>23:
                return ['calc_clock_angle',"错误的小时格式"]
            if sMinute < 0 or sMinute>60:
                return ['calc_clock_angle',"错误的分针格式"]
            if sSecond < 0 or sSecond>60:
                return ['calc_clock_angle',"错误的秒针格式"]

            angleSecond = sSecond * 360.0 / 60
            angleMinute = sMinute * (360.0 / 60) + sSecond / 10.0
            angleHour = sHour * 30.0  + sMinute * (30.0 / 60) + sSecond * (30.0 /(60 * 60))
            
            return ['new_call',"输入时间:{}\n时针角度:{:.4f}\n分针角度:{:.4f}\n秒针角度:{:.4f}".format(inTime,angleHour,angleMinute,angleSecond)]

        except:
            return ['calc_clock_angle',"请输入要计算的时间，以HH:MI:SS的格式,例如04:35:00"]