from message3 import message3

def hyperna_msg3():
    print("REMEMBER:")
    print("Sodium contents: ")
    print(" GORS: 75 mmol/l ")
    print(" 1/2 NS: 77 mmol/l")
    print(" 1/2 Acetate: 66 mmol/l \n")

def hyperna_calc3():
    print("FLUID VOLUME CALCULATION")
    wt = input(" Weight (kg): ")
    serum = input(" Serum Sodium (mmol/l): ")
    fluid = input(" Sodium in correction fluid (mmol/l): ")

    corr = ((10/((float(serum)-float(fluid))/((float(wt)*0.6)+1)))*1000)/24
    print("\nCorrection volume:", corr, "ml/hr\n")

    print("25% DIET CURTAIL")
    diet = input(" Enter full diet vol (ml/2h):  ")
    curt = float(diet)*0.75 
    print(" \n25% curtailed volume", curt, "ml/2h + Salt added.")

hyperna_msg3()
hyperna_calc3()
#raw_input("Press `Enter' to exit.")
