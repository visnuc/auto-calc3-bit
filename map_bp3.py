from message3 import message3

def map_bp3():
    sbp = float(input(" Systolic BP (mmHg): "))
    dbp = float(input("Diastolic BP (mmHg): "))
    map_bp = (dbp*2 + sbp)/3
    # MAP formula 2:
    # map_bp = ((sbp-dbp)/3)+dbp
    print("\nMAP is", round(map_bp, 2), "mmHg\
\n[Reference: Child >50; Adult >65] \n")
    ques = str(input("Want to do anything else? (y/n): "))
    if ques == "y" or ques == "Y":
        from main3 import main3
    else:
        print("Thanks for using auto-calc!")
        exit()

map_bp3()
#input("Please press `Enter' to exit")
