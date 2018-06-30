import sys
from message3 import message3

def sevdh3():
    wt = float(input("Weight (kg): "))
    raw_age = str(input("Age less than 1 yr? (y/n): "))
    age_n = float(input("Patient's age (number only): "))
    if raw_age == "Y" or raw_age == "y":
        age = float(age_n/12)
    elif raw_age == "N" or raw_age == "n":
        age = age_n
    else:
        print("Please restart the application!")
        input("Press `Enter' to restart")
        sys.exit()
    sam = str(input("SAM(1) / NON-SAM(2): "))
    if sam == "1":
        if age < 0.16666:
            print("\n1st hr:", round(wt*20, 2), "ml IV only (1/2 AC +5% Dex +13 KCL)")
            print("2nd hr:", round(wt*10, 2), "ml IV (1/2 AC +5% Dex +13 KCL) +", \
                  round(wt*10, 2), "ml oral (GORS)")
            print("3rd, 4th hr:", round(wt*10, 2), "ml/hr (GORS)")
            print("Next 8-10 hrs:", round(wt*5, 2), "ml/hr (GORS), \
till correction")
        elif age >= 0.16666:
            print("\n1st hr:", round(wt*20, 2), "ml IV only (AC +5% Dex +7 KCL)")
            print("2nd hr:", round(wt*10, 2), "ml IV (AC +5% Dex +7 KCL) +", \
                  round(wt*10, 2), "ml oral (GORS)")
            print("3rd, 4th hr:", round(wt*10, 2), "ml/hr (GORS)")
            print("Next 8-10 hrs:", round(wt*5, 2), "ml/hr (GORS), \
till correction\n")
    elif sam == "2":
        if age < 0.16666:
            print("\n")
            print(round(wt*30, 2), "ml in 1 hr (1/2 AC/NS), then")
            print(round(wt*70, 2), "ml in 5 hrs (1/2 AC/NS)\n")
        elif age >= 0.16666 and age < 1:
            print("\n")
            print(round(wt*30, 2), "ml in 1 hr (AC/NS), then")
            print(round(wt*70, 2), "ml in 5 hrs (AC/NS)\n")
        elif age >= 1:
            print("\n")
            print(round(wt*30, 2), "ml in 1/2 hr (AC/NS), then")
            print(round(wt*70, 2), "ml in 2.5 hrs (AC/NS)\n")
    else:
        print("Please restart the application.")

sevdh3()
