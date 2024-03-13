import asyncio
import time
from infinitecraft import InfiniteCraft
import infinitecraft

async def main():
    async with InfiniteCraft() as game:
        print(game.discoveries)
asyncio.run(main())