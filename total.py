import asyncio
import random
import time
from infinitecraft import InfiniteCraft

async def main():
    async with InfiniteCraft() as game:
        print(f"Total: {len(game.discoveries)}.")

if __name__ == "__main__":
    asyncio.run(main())
