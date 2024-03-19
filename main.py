import asyncio
import craft
import custom
import individual
import total
from termcolor import colored

print(colored("""
------------------------ INFINITEBOT ------------------------
Created by Carson Bates and Elouan Grimm

""", "light_blue"))
while True:
  try:
    option = input(colored("""Main Menu: 
    1: Random Run (Recomended)
    2: Individual (Run the program on one item)
    3: Custom (Run one custom pair)
    4: View Total Elements

Option (1, 2, 3, 4, Quit): """, "light_grey"))

    if option == "1" or option == "":
      try:
        print(colored("""

------------------------ Starting Random Run ------------------------
                """, "light_red"))
        asyncio.run(craft.main())
      except asyncio.TimeoutError as ex:
        print("There was a timeout error:" + str(ex) +
              "This is normal. The file should run again.")
        asyncio.run(craft.main())
      except KeyboardInterrupt:
        print("""

------------------------ Quiting ------------------------
                  """)
        asyncio.run(total.main())
        print("""

  """)
        exit()

    if option == "2":
      try:
        print(colored("""

------------------------ Starting Individual ------------------------
                """, "light_red"))
        asyncio.run(individual.main())
      except asyncio.TimeoutError:
        print("There was a timeout error. This is normal. The file should run again.")
        asyncio.run(individual.main())
      except KeyboardInterrupt:
        print("""

------------------------ Quiting ------------------------
                  """)
        asyncio.run(total.main())
        print("""

  """)
        exit()

    if option == "3":
      try:
        print(colored("""

------------------------ Starting Custom ------------------------
                """, "light_red"))
        asyncio.run(custom.main())
      except asyncio.TimeoutError as ex:
        print("There was a timeout error:" + str(ex) +
              "This is normal. The file should run again.")
        asyncio.run(custom.main())
      except KeyboardInterrupt:
        print("""

------------------------ Quiting ------------------------
                  """)
        asyncio.run(total.main())
        print("""

  """)
        exit()
        
    if option == "4":
          print(colored("""


------------------------------------------------ """, "light_red"))
          asyncio.run(total.main())
          print("""

  """)
          
    if option == "Quit":
        print("""

------------------------ Quiting ------------------------
              """)
        exit()
  except KeyboardInterrupt:
    print("\n")
    exit()
