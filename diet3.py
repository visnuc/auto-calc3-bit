def diet3():
    wt = float(input("Weight [kg]: "))
    each_feed = float(input("Each feed [ml]: "))
    interval = float(input("Interval [hr]: "))
    times = 24/interval
    t_vol = (each_feed*times)/wt
    kind = str(input("MIF/MS/MS100/FSRS [1|2|3|4]: "))
    if kind == "1":
        t_cal = t_vol*0.68
    elif kind == "2":
        t_cal = t_vol*0.67
    elif kind == "3":
        t_cal = t_vol*1.0
    elif kind == "4":
        t_cal = t_vol*0.70
    print("\nDaily dietary volume:", t_vol, "ml/kg/day")
    print("Daily calorie intake:", t_cal, "kcal/kg/day\n")

diet3()
