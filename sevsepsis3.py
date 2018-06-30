from message3 import message3

def sevsepsis3():
    wt = float(input("Weight (kg): "))
    sam = str(input("SAM-SUW(1) Non-SAM(2): "))
    if sam == "1":
        bolus = float(wt*20)
        bt = float(wt*10)
        print("\nIn Children:")
        print("Bolus 1:", round(bolus, 2), "ml in 1 hr (HS/NS),", "If MAP <50")
        print("Bolus 2:", round(bolus, 2), "ml in 1 hr (HS/NS),", "If MAP <50")
        print("Bolus 3:", round(bt, 2), "ml WBT,", "If MAP <50 mmHg")
        print("START Ionotropes, monitor BP every 15 min\n")
    elif sam == "2":
        bolus = float(wt*20)
        print("\nIn Children:")
        print("\nBolus 1:", round(bolus, 2), "ml in 30 min (HS/NS),", "If MAP <50")
        print("Bolus 2:", round(bolus, 2), "ml in 30 min (HS/NS),", "If MAP <50")
        print("Bolus 3:", round(bolus, 2), "ml in 30 min (HS/NS),", "If MAP <50")
        print("START Ionotropes, monitor BP every 15 min\n")

sevsepsis3()
