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
                print(f"{result} = {game.discoveries[i]} + {game.discoveries[j]}. TOTAL: {str(len(game.discoveries))}")
                file = open("recipies.txt", "a")
                file.write(f"\n{result} = {game.discoveries[i]} + {game.discoveries[j]}")
                file = open("discoveries.txt", "a")
                file.write(f"\n{result}")

if __name__ == "__main__":
    asyncio.run(main())
