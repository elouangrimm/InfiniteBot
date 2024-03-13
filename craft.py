import asyncio
import random
import time
from infinitecraft import InfiniteCraft

async def main():
    async with InfiniteCraft() as game:
        while True:
            await asyncio.sleep(0.1)
            i = random.randint(0, len(game.discoveries))
            j = random.randint(0, len(game.discoveries))
            if i < len(game.discoveries) - 1 and j < len(game.discoveries) - 1:
                result = await game.pair(game.discoveries[i], game.discoveries[j])
                print(f"{result} = {game.discoveries[i]} + {game.discoveries[j]}")
                file = open("discoveries_parents.txt", "a")
                file.write(f"\n{game.discoveries[i]}+{game.discoveries[j]}={result}")

asyncio.run(main()) 