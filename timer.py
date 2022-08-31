import asyncio

class Timer:

    def __init__(self, hour, minute, second) -> None:
        self.hour = hour * 3600
        self.minute = minute * 60
        self.second = second

    async def set_timer(self):
        await asyncio.sleep(self.hour + self.minute + self.second)
        print('Time\'s up!')

    def run_timer(self):
        asyncio.run(self.set_timer())


if __name__ == '__main__':
    jija = Timer(0, 0, 5)
    jija.run_timer()
    pass
