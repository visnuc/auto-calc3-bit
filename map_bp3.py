from message3 import message3

def map_bp3():
    sbp = float(input(" Systolic BP (mmHg): "))
    dbp = float(input("Diastolic BP (mmHg): "))
    map_bp = (dbp*2 + sbp)/3
    # MAP formula 2:
    # map_bp = ((sbp-dbp)/3)+dbp
    print("\nMAP is", round(map_bp, 2), "mmHg\
\n[Reference (mmHg): Child >50; Adult >65] \n")

map_bp3()
#input("Please press `Enter' to exit")
