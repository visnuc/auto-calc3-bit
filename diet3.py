def diet3():
    wt = float(input("  Weight (kg): "))
    each_feed = float(input("Feed vol (ml): "))
    interval = float(input("Interval (hr): "))
    times = 24/interval
    t_vol = (each_feed*times)/wt
    kind = str(input(" (1) MIF\
\n (2) MS\
\n (3) MS100\
\n (4) FSRS\
\n (5) 3/4 FSRS\
\n (6) Soyabased formula\
\n (7) 3/4 Soyabased formula\
\nEnter code: "))
    if kind == "1" or kind == "6":
        t_cal = t_vol*0.68
    elif kind == "2":
        t_cal = t_vol*0.67
    elif kind == "3":
        t_cal = t_vol*1.0
    elif kind == "4":
        t_cal = t_vol*0.70
    elif kind == "5":
        t_cal = t_vol*0.566
    elif kind == "7":
        t_cal = t_vol*0.51
    else:
        print("Please try again.")
    print("\nVolume :", round(t_vol, 2), "ml/kg/day")
    print("Calorie:", round(t_cal, 2), "kcal/kg/day \n")
    ques = str(input("Want to do anything else? (y/n): "))
    if ques == "y" or ques == "Y":
        from main3 import main3
    else:
        print("Thanks for using auto-calc!")
        exit()
        

diet3()
