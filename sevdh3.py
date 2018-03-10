import sys
from message3 import message3

def sevdh3():
    wt = float(input("Weight (kg): "))
    raw_age = str(input("Patient less than 1 yr old? [y/n]: "))
    age_n = float(input("Patient's age [number only]: "))
    if raw_age == "Y" or raw_age == "y":
        age = float(age_n/12)
    elif raw_age == "N" or raw_age == "n":
        age = age_n
    else:
        print("Please restart the application!")
        input("Press `Enter' to restart")
        sys.exit()
    sam = str(input("SAM / NON-SAM? [1/2]: "))
    if sam == "1":
        if age < 0.166:
            print("\n 1st hr:", wt*20, "IV only (1/2 AC + 5% Dex + 13 KCL)")
            print(" 2nd hr:", wt*10, "ml IV (1/2 AC + 5% Dex + 13 KCL) +", \
                  wt*10, "ml oral (GORS)")
            print(" 3rd and 4th hr:", wt*10, "ml/hr (GORS)")
            print(" Next 8-10 hrs:", wt*5, "ml/hr (GORS), \
till dehydration correction")
        elif age >= 0.166:
            print("\n 1st hr:", wt*20, "IV only (1/2 AC + 5% Dex + 7 KCL)")
            print(" 2nd hr:", wt*10, "ml IV (1/2 AC + 5% Dex + 13 KCL) +", \
                  wt*10, "ml oral (GORS)")
            print(" 3rd and 4th hr:", wt*10, "ml/hr (GORS)")
            print(" Next 8-10 hrs:", wt*5, "ml/hr (GORS), \
till dehydration correction\n")
    else:
        if age < 1:
            print("\n")
            print("", wt*30, "ml in 1 hr (AC/NS), then")
            print("", wt*70, "ml in 5 hrs (AC/NS)\n")
        elif age >= 1:
            print("\n")
            print("", wt*30, "ml in 1/2 hr (AC/NS), then")
            print("", wt*70, "ml in 2.5 hrs (AC/NS)\n")

sevdh3()
