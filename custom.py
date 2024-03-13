import asyncio
import time
from infinitecraft import InfiniteCraft
import infinitecraft

name1 = input("Element 1: ")
name2 = input("Element 2: ")

async def main():
    async with InfiniteCraft() as game:
        print(
            f"Pairing elements: {name1} and " + name2
        )
        element1 = infinitecraft.Element()
        element1.name = name1
        
        element2 = infinitecraft.Element()
        element2.name = name2
        result = await game.pair(element1,
                                 element2)
        print(f"Result: {result}")
        print(f"Total: {len(game.discoveries)}")
        file = open("discoveries.txt", "a")
        file.write(
            f"\n{name1}+" + name2 + f"={result}"
        )

asyncio.run(main())
