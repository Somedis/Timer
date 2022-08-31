from datetime import datetime
import asyncio

class TimeNow:

    now = datetime.now()

    def __str__(self) -> str:
        return f'{self.now.hour}:{self.now.minute}:{self.now.second}'

    @classmethod
    def time_now(cls):
        return (cls.now.hour, cls.now.minute, cls.now.second)


class OutputTimeNow:

    async def output_time(self):
        time = TimeNow()
        while True:
            print(time)
            await asyncio.sleep(1)

    def run_output_time(self):
        asyncio.run(self.output_time())


class InputTime:

    def __init__(self) -> None:
        hour = int(input('Hours: '))
        minute = int(input('Minutes: '))
        second = int(input('Seconds: '))
        if __class__.check_value(minute) and __class__.check_value(second):
            self.hour = hour
            self.minute = minute
            self.second = second
        else:
            raise ValueError('Out of range')

    def __repr__(self) -> str:
        return f'{self.hour}:{self.minute}:{self.second}'

    @classmethod
    def check_value(cls, value):
        return 0 <= value <= 60

    def get_inputtime(self):
        return (self.hour, self.minute, self.second)


if __name__ == '__main__':
    test = TimeNow()
    print(test)
    test1 = InputTime()
    print(test1)
    print(test1.__dict__)
    pass