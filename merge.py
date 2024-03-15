import asyncio
import random
import time
import json
from infinitecraft import InfiniteCraft

async def main():
    async with InfiniteCraft() as game:
        i = 0
        filtered = 0
        filtered_name_list = []
        for discovery in game.discoveries:
            i += 1
            j = 0
            for discovery_layer2 in game.discoveries:
                j += 1
                if discovery.name == discovery_layer2.name and not i == j and not discovery.name in filtered_name_list:
                    game.discoveries.remove(discovery_layer2)
                    filtered_name_list.append(discovery.name)
                    filtered += 1

            print(f"Layer: {i}, Filtered: {filtered}")
        raw_discoveries = compile_json(game.discoveries)
        with open("discoveries.json", "w") as file:
            file.write(raw_discoveries)


def compile_json(discoveries_list):
    return_json = "["

    for discovery in discoveries_list:
        if discovery.is_first_discovery:
            first_string = 'true'
        else:
            first_string = 'false'
        return_json += '\n{\n\t"name": "'+discovery.name+'",\n\t"emoji": "'+str(discovery.emoji)+'",\n\t"is_first_discovery": '+first_string+'\n},'

    return_json += "]"
    return return_json

            
asyncio.run(main())