# -*- coding: UTF-8 -*-


class ClockAngle:

    def calcAngle(self, sSecond, sMinute, sHour):
        angleSecond = sSecond * 360.0 / 60
        angleMinute = sMinute * (360.0 / 60) + sSecond / 10.0
        angleHour = sHour * 30.0 + sMinute * \
            (30.0 / 60) + sSecond * (30.0 / (60 * 60))
        return angleSecond, angleMinute, angleHour

    def calcClockAngle(self, inUserSaid):
        stepID = inUserSaid['step_id'] + 1
        inTime = inUserSaid['message']

        if stepID == 1:
            returnKey = {'callback_key': 'calc_clock_angle',
                         'message': "请输入要计算的时间，以HH:MI:SS的格式,例如04:35:00",
                         'step_id': stepID}
        else:
            try:
                dTimeDetail = inTime.split(":")
                sHour = int(dTimeDetail[0])
                sMinute = int(dTimeDetail[1])
                sSecond = int(dTimeDetail[2])
                # 检查输入的数值
                if sHour > 12 and sHour <= 23:
                    sHour = sHour - 12
                if sHour > 23:
                    returnKey = {'callback_key': 'calc_clock_angle',
                                 'message': "错误的小时格式", 'step_id': stepID}
                if sMinute < 0 or sMinute > 60:
                    returnKey = {'callback_key': 'calc_clock_angle',
                                 'message': "错误的分针格式", 'step_id': stepID}
                if sSecond < 0 or sSecond > 60:
                    returnKey = {'callback_key': 'calc_clock_angle',
                                 'message': "错误的秒针格式", 'step_id': stepID}
                angleSecond, angleMinute, angleHour = self.calcAngle(
                    sSecond, sMinute, sHour)
                returnKey = {'message': "输入时间:\t{}\n时针角度:\t{:.4f}\n分针角度:\t{:.4f}\n秒针角度:\t{:.4f}".format(
                    inTime, angleHour, angleMinute, angleSecond), 'step_id': 0, 'callback_key': 'list_function'}
            except:
                returnKey = {'callback_key': 'calc_clock_angle',
                             'message': "请输入要计算的时间，以HH:MI:SS的格式,例如04:35:00", 'step_id': 1}
        return {**inUserSaid, **returnKey}

    def calcHourMinute(self, inUserSaid):
        stepID = inUserSaid['step_id'] + 1
        inTime = inUserSaid['message']
        return_message = ['']
        if stepID == 1:
            returnKey = {'callback_key': 'calc_hour_minute',
                         'message': "请以下面的格式输入：开始小时，结束小时，角度；例如：4,5,90",
                         'step_id': stepID}
        else:
            try:
                inTimeList = inTime.split(",")
                hourStart = int(inTimeList[0])
                hourEnd = int(inTimeList[1])
                angleMatch = int(inTimeList[2])
                return_message.append('='*28)
                for iHour in range(hourStart, hourEnd, 1):
                    for iMinute in range(0, 60):
                        for iSecond in range(0, 60):
                            angleSecond, angleMinute, angleHour = self.calcAngle(
                                iSecond, iMinute, iHour)
                            if round(abs(angleHour - angleMinute), 1) == angleMatch + 0.0:
                                return_message.append('\t{}:{}:{}'.format(
                                    iHour, iMinute, iSecond))
                                return_message.append('='*28)
                                return_message.append('时针角度:\t{:.4f}\n分针角度:\t{:.4f}\n秒针角度:\t{:.4f}'.format(
                                    angleHour, angleMinute, angleSecond))
                                return_message.append('='*28)
                returnKey = {'callback_key': 'list_function',
                         'message': '\n'.join(return_message),
                         'step_id': stepID}
            except:
                returnKey = {'callback_key': 'calc_hour_minute',
                         'message': "请以下面的格式输入：开始小时，结束小时，角度；例如：4,5,90",
                         'step_id': 1}
        return {**inUserSaid, **returnKey}        
