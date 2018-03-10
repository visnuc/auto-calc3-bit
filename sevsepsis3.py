from message3 import message3

def sevsepsis3():
    wt = float(input("Weight (kg): "))
    sam = str(input("SAM-SUW / Non-SAM [1/2]: "))
    if sam == "1":
        bolus = float(wt*20)
        bt = float(wt*10)
        print("\n In Children:")
        print(" Bolus 1:", bolus, "ml in 1 hr (HS/NS),", "If MAP <50")
        print(" Bolus 2:", bolus, "ml in 1 hr (HS/NS),", "If MAP <50")
        print(" Bolus 3:", bt, "ml WBT,", "If MAP <50 mmHg")
        print(" START Ionotropes, monitor BP every 15 min\n") 
    elif sam == "2":
        bolus = float(wt*20)
        print("\n In Children:")
        print(" Bolus 1:", bolus, "ml in 30 min (HS/NS),", "If MAP <50")
        print(" Bolus 2:", bolus, "ml in 30 min (HS/NS),", "If MAP <50")
        print(" Bolus 3:", bolus, "ml in 30 min (HS/NS),", "If MAP <50")
        print(" START Ionotropes, monitor BP every 15 min\n")

sevsepsis3()
