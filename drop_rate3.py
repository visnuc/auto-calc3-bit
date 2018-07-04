from message3 import message3

def drop_rate3():
    vol = float(input("\nRequired IV volume (ml): "))
    hr = float(input("Intended time (hr): "))
    drop_fac = str(input("Infusion set type:\
\n (1) Blood set\
\n (2) Regular set\
\n (3) Micro-burette set\
\nEnter code: "))
    if drop_fac == "1":
        inf_set = 10
    elif drop_fac == "2":
        inf_set = 15
    elif drop_fac == "3":
        inf_set = 60
    dpm = (vol*inf_set)/(hr*60)
    if drop_fac == "1":
        print("\nAt", int(dpm), "drops/min", round(vol, 2), "ml IV will take ~", int(hr), "hrs")
        print("Drop factor : 1 ml =", inf_set, "drops\n")
    elif drop_fac == "2":
        print("\nAt", int(dpm), "drops/min", round(vol, 2), "ml IV will take ~", int(hr), "hrs")
        print("Drop factor : 1 ml =", inf_set, "drops\n")
    elif drop_fac == "3":
        print("\nAt", int(dpm), "drops/min", round(vol, 2), "ml IV will take ~", int(hr), "hrs")
        print("Drop factor : 1 ml =", inf_set, "microdrops\n")
    ques = str(input("Want to do anything else? (y/n): "))
    if ques == "y" or ques == "Y":
        from main3 import main3
    else:
        print("Thanks for using auto-calc!")
        exit()

drop_rate3()
