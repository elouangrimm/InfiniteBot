import asyncio
import craft
import custom
import individual

print("""------------------------ INFINITEBOT ------------------------
Created by Carson Bates and Elouan Grimm

""")
option = input("""Pick an option: 
1: Random Run (Recomended)
2: Individual (Run the program on one item)
3: Custom (Run one custom pair)

Option (1, 2, 3, Quit): """)

if option == "1":
  try:
    print("""

------------------------ Starting Random Run ------------------------
            """)
    asyncio.run(craft.main())
  except asyncio.TimeoutError as ex:
    print("There was a timeout error:" + str(ex) +
          "This is normal. The file should run again.")
    asyncio.run(craft.main())
  except KeyboardInterrupt:
    print("""

    ------------------------ Quiting ------------------------
              """)
    exit()

if option == "2":
  try:
    print("""

  ------------------------ Starting Individual ------------------------
            """)
    asyncio.run(individual.main())
  except asyncio.TimeoutError as ex:
    print("There was a timeout error:" + str(ex) +
          "This is normal. The file should run again.")
    asyncio.run(craft.main())
  except KeyboardInterrupt:
    print("""

    ------------------------ Quiting ------------------------
              """)
    exit()

if option == "3":
  try:
    print("""

  ------------------------ Starting Custom ------------------------
            """)
    asyncio.run(custom.main())
  except asyncio.TimeoutError as ex:
    print("There was a timeout error:" + str(ex) +
          "This is normal. The file should run again.")
    asyncio.run(craft.main())
  except KeyboardInterrupt:
    print("""

    ------------------------ Quiting ------------------------
              """)
    exit()

if option == "Quit":
  print("""

------------------------ Quiting ------------------------
          """)
  exit()
