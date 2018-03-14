from message3 import message3 # imports the function called message3, from the file named message3

choice = str(input("Choose from the list :\
\n [1] Hypernatremia\
\n [2] Severe Sepsis\
\n [3] Severe Dehydration\
\n [4] Some Dehydration\
\n [5] `X'% dehydration\
\n [6] MAP calculation\
\n [7] Daily Diet Volume\
\n[1|2|3|4|5|6|7]: "))
if choice == "1":
    from hyperna3 import hyperna_msg3
    from hyperna3 import hyperna_calc3
elif choice == "2":
    from sevsepsis3 import sevsepsis3
elif choice == "3":
    from sevdh3 import sevdh3
elif choice == "4":
    from somedh3 import somedh3
elif choice == "5":
    from xdh3 import xdh3
elif choice == "6":
    from map_bp3 import map_bp3
elif choice == "7":
    from diet3 import diet3
else:
    print("Please try again.")

input("Press `Enter' to exit.")
