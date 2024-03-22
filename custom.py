import asyncio
import time
from infinitecraft import InfiniteCraft
import infinitecraft

async def main():
    async with InfiniteCraft() as game:
        inputelement1 = input("Element 1: ")
        inputelement2 = input("Element 2: ")
        print(
            f"Pairing elements: {inputelement1} and " + inputelement2
        )
        element1 = infinitecraft.Element()
        element1.name = inputelement1
        
        element2 = infinitecraft.Element()
        element2.name = inputelement2
        result = await game.pair(element1,
                                 element2)
        print(f"Result: {result}")
        print(f"Total: {len(game.discoveries)} \n")
        file = open("discoveries.txt", "a")
        file.write(
            f"\n{result} = {inputelement1} + {inputelement2}"
        )

if __name__ == "__main__":
    asyncio.run(main())