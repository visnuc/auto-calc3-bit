from message3 import message3

def map_bp3():
    sbp = float(input(" Systolic BP (mmHg): "))
    dbp = float(input("Diastolic BP (mmHg): "))
    map_bp3 = (dbp*2 + sbp)/3
    # MAP formula 2:
    # map_bp3 = ((sbp-dbp)/3)+dbp
    print("\n MAP is", map_bp3, "mmHg\n")

map_bp3()
#input("Please press `Enter' to exit")
