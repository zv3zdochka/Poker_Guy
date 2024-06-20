import asyncio

from Utils import Utils


class Game(Utils):
    def __init__(self):
        super().__init__()

    async def check_active(self):
        while True:
            st = self.check_buttons_right()
            if not st:
                await asyncio.sleep(2)
                print('wait')
            else:
                return

    async def play(self):
        while True:
            await self.check_active()
            await self.take_cards()
            await self.take_amount()



poker = Game()
asyncio.run(poker.play())