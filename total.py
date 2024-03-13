import asyncio
import random
import time
from infinitecraft import InfiniteCraft

async def main():
    async with InfiniteCraft() as game:
        print(f"Total: {len(game.discoveries)}.")

asyncio.run(main()) 