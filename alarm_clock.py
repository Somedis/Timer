from timer import Timer
from _time import TimeNow
import asyncio


class AlarmClock(Timer):

    DAY = 86400
    HOUR_NOW, MINUTE_NOW, SECOND_NOW = TimeNow.time_now()

    @classmethod
    def time_in_second(cls):
        secondNow = cls.HOUR_NOW * 3600 + cls.MINUTE_NOW * 60 + cls.SECOND_NOW
        return secondNow

    def set_time(self):
        inputTime = self.hour + self.minute + self.second
        if __class__.time_in_second() < inputTime:
            return inputTime - __class__.time_in_second()
        elif __class__.time_in_second() > inputTime:
            return (__class__.DAY - __class__.time_in_second()) + inputTime
        else:
            return 0

    async def set_alarmClock(self):
        await asyncio.sleep(self.set_time())
        print('Time\'s up!')

    def run_alarmClock(self):
        asyncio.run(self.set_alarmClock())



if __name__ == '__main__':
    jija = AlarmClock(16, 24, 50)
    jija.run_alarmClock()
    pass