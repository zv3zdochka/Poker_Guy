import asyncio

from Utils import Utils


class Game(Utils):
    # n players at the table
    def __init__(self):
        super().__init__()
        self.n = self.get_players()

    def get_players(self):
        return 1

    def collect_data(self):
        pass

    def select_money(self):
        # in process
        pass

    async def check_active(self):
        while True:
            st = self.check_buttons_right()
            if not st:
                await asyncio.sleep(2)
                print('wait')
            else:
                return

    async def play(self):
        # all previous staff like select game and amount of money
        await self.check_active()
        print(333)


poker = Game()
asyncio.run(poker.play())