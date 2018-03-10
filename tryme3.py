from message3 import message3

choice = str(input("Choose from the list :\
\n [1] Hypernatremia\
\n [2] Severe Sepsis\
\n [3] Severe Dehydration\
\n [4] Some Dehydration\
\n [5] MAP calculation\
\n[1/2/3/4/5]: "))
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
    from map_bp3 import map_bp3
else:
    print("Please try again.")

input("Press `Enter' to exit.")
