# -*- coding: UTF-8 -*-


class ClockAngle:

    def calcAngle(self, sSecond, sMinute, sHour):
        angleSecond = sSecond * 360.0 / 60
        angleMinute = sMinute * (360.0 / 60) + sSecond / 10.0
        angleHour = sHour * 30.0 + sMinute * \
            (30.0 / 60) + sSecond * (30.0 / (60 * 60))
        return angleSecond, angleMinute, angleHour

    def calcClockAngle(self, inUserSaid):
        inStep = inUserSaid[1]
        inTime = inUserSaid[0]
        if inStep == '0':
            return ['calc_clock_angle', "请输入要计算的时间，以HH:MI:SS的格式,例如04:35:00", '1']
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
                    return ['calc_clock_angle', "错误的小时格式", '1']
                if sMinute < 0 or sMinute > 60:
                    return ['calc_clock_angle', "错误的分针格式", '1']
                if sSecond < 0 or sSecond > 60:
                    return ['calc_clock_angle', "错误的秒针格式", '1']

                angleSecond, angleMinute, angleHour = self.calcAngle(
                    sSecond, sMinute, sHour)

                return ['list_function', "输入时间:\t{}\n时针角度:\t{:.4f}\n分针角度:\t{:.4f}\n秒针角度:\t{:.4f}".format(inTime, angleHour, angleMinute, angleSecond), '0']

            except:
                return ['calc_clock_angle', "请输入要计算的时间，以HH:MI:SS的格式,例如04:35:00", '1']
    def calcHourMinute(self, inUserSaid):
        inStep = inUserSaid[1]
        inTime = inUserSaid[0]
        if inStep == '0':
            return ['calc_hour_minute', "请以下面的格式输入：开始小时，结束小时，角度；例如：4,5,90", '1']
        else:
            try:

                inTimeList = inTime.split(",")
                hourStart = int(inTimeList[0])
                hourEnd = int(inTimeList[1])
                angleMatch = int(inTimeList[2])
                print('='*28)
                for iHour in range(hourStart, hourEnd, 1):
                    for iMinute in range(0, 60):

                        for iSecond in range(0, 60):
                            angleSecond, angleMinute, angleHour = self.calcAngle(
                                iSecond, iMinute, iHour)
                            if round(abs(angleHour - angleMinute), 1) == angleMatch + 0.0:
                                print('\t{}:{}:{}'.format(
                                    iHour, iMinute, iSecond))
                                print('='*28)
                                print('时针角度:\t{:.4f}\n分针角度:\t{:.4f}\n秒针角度:\t{:.4f}'.format(
                                    angleHour, angleMinute, angleSecond))
                                print('='*28)
                return ['list_function', "计算完成", '0']

            except:
                return ['calc_hour_minute', "请以下面的格式输入：开始小时，结束小时，角度；例如：4,5,90", '1']

