from message3 import message3

def hyperna_msg3():
    print("Sodium contents: ")
    print(" G-ORS : 75 mmol/l ")
    print(" 1/2 NS: 77 mmol/l")
    print(" 1/2 AC: 66 mmol/l \n")

def hyperna_calc3():
    print("FLUID VOLUME CALCULATION")
    wt = float(input(" Weight (kg): "))
    serum = input(" Serum Sodium (mmol/l): ")
    fluid = input(" Fluid Sodium (mmol/l): ")

    corr = ((10/((float(serum)-float(fluid))/((float(wt)*0.6)+1)))*1000)/24
    print("\nCorrection volume:", round(corr, 2), "ml/hr\n")

    print("25% DIET CURTAIL")
    kwash = str(input(" Marasmus(1) | Kwash(2): "))
    if kwash == "1":
        curt = (wt*10)*0.75
    elif kwash == "2":
        curt = (wt*9)*0.75
    print("\nCurtailed diet:", round(curt, 2), "ml/2h + Salt added.")

hyperna_msg3()
hyperna_calc3()
#input("Press `Enter' to exit.")
