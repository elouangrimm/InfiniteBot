import asyncio
import random
import time
import json
from infinitecraft import InfiniteCraft
import os
import platform

async def main():
    clear_code = "clear"

    if platform.system() == "Windows":
        clear_code = "cls"

    async with InfiniteCraft() as game:
        discoveries_length = len(game.discoveries)
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

            print("STATUS: REMOVING DUPLICATES")
            print(f"Layer: {i}, Filtered: {filtered} | {int(i/(discoveries_length) * 100)}%")
            os.system(clear_code)
        raw_discoveries = compile_json(game.discoveries, clear_code)
        with open("discoveries.json", "w") as file:
            file.write(raw_discoveries)


def compile_json(discoveries_list, clear_code):
    return_json = "["
    discoveries_length = len(discoveries_list)
    i = 0

    for discovery in discoveries_list:
        i += 1
        if discovery.is_first_discovery:
            first_string = 'true'
        else:
            first_string = 'false'
        return_json += '\n{\n\t"name": "'+discovery.name+'",\n\t"emoji": "'+str(discovery.emoji)+'",\n\t"is_first_discovery": '+first_string+'\n},'
        
        print("STATUS: PARSING TO JSON")
        print(f"{int(i/(discoveries_length) * 100)}%")
        os.system(clear_code)

    return_json += "]"
    return return_json

            
asyncio.run(main())