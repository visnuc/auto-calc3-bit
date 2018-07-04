from message3 import message3
# imports the function called message, from the file named message

choice = str(input("Choose your module: \
\n [1] Hypernatremia\
\n [2] Fluid \
\n [3] MAP \
\n [4] Diet\
\n [5] Drops/min\
\nEnter the code [1-5]: "))
if choice == "1":
    from hyperna3 import hyperna_msg3
    from hyperna3 import hyperna_calc3
elif choice == "2":
    choice_2 = str(input("Choose from the list:\
        \n [1] Severe Sepsis\
        \n [2] Severe Dehydration\
        \n [3] Some Dehydration\
        \n [4] `X'% dehydration\
        \nEnter the code [1-4]: "))
    if choice == "2" and choice_2 == "1":
        from sevsepsis3 import sevsepsis3
    elif choice == "2" and choice_2 == "2":
        from sevdh3 import sevdh3
    elif choice == "2" and choice_2 == "3":
        from somedh3 import somedh3
    elif choice == "2" and choice_2 == "4":
        from xdh3 import xdh3
elif choice == "3":
    from map_bp3 import map_bp3
elif choice == "4":
    from diet3 import diet3
elif choice == "5":
    from drop_rate3 import drop_rate3
else:
    print("Please try again.")

#input("Press `Enter' to exit.")
input("Press `Enter' to exit.")
