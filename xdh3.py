def xdh3():
    x = float(input("\nPercentage(%) of dehydration (number only): "))
    wt = float(input("Weight (kg): "))
    xdh_corr = wt*(x*10)
    print(round(xdh_corr, 2), "ml in 4-6 hrs\n")
    ques = str(input("Want to do anything else? (y/n): "))
    if ques == "y" or ques == "Y":
        from main3 import main3
    else:
        print("Thanks for using auto-calc!")
        exit()
        

xdh3()

#input("Please press `Enter' to exit.")
