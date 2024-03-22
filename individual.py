import asyncio
import time
from infinitecraft import InfiniteCraft
import infinitecraft


async def main():
  async with InfiniteCraft() as game:
    inputelement = input("Element: ")
    while True:
      for i in range(len(game.discoveries) - 1):
        await asyncio.sleep(0.2)
        if i < len(game.discoveries) - 1:
          element = infinitecraft.Element()
          element.name = inputelement
          result = await game.pair(game.discoveries[i], element)
          print(f"{result} = {game.discoveries[i]} + {inputelement}. TOTAL: {len(game.discoveries)}")
          file = open("discoveries.txt", "a")
          file.write(f"\n{game.discoveries[i]}+" + inputelement + f"={result}")


if __name__ == "__main__":
  asyncio.run(main())
