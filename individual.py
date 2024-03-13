import asyncio
import time
from infinitecraft import InfiniteCraft
import infinitecraft

name = input("Element: ")

async def main():
    async with InfiniteCraft() as game:
        while True:
            for i in range(len(game.discoveries) - 1):
                await asyncio.sleep(0.2)
                if i < len(game.discoveries) - 1:
                    print(
                        f"Pairing elements: {game.discoveries[i]} and " + name
                    )
                    element = infinitecraft.Element()
                    element.name = name
                    result = await game.pair(game.discoveries[i],
                                                element)
                    print(f"Result: {result}")
                    print(f"Total: {len(game.discoveries)}")
                    file = open("discoveries.txt", "a")
                    file.write(
                        f"\n{game.discoveries[i]}+" + name + f"={result}"
                    )

asyncio.run(main())
