import craft
import individual
import custom
import asyncio

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
    except:
        exit()

if option == "2":
    print("""

------------------------ Starting Individual ------------------------
          """)
    asyncio.run(individual.main())

if option == "3":
    print("""

------------------------ Starting Custom ------------------------
          """)
    asyncio.run(custom.main())

if option == "Quit":
    print("""

------------------------ Quiting ------------------------
          """)
    exit()