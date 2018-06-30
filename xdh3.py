def xdh3():
    x = float(input("\nPercentage(%) of dehydration (number only): "))
    wt = float(input("Weight (kg): "))
    xdh_corr = wt*(x*10)
    print(round(xdh_corr, 2), "ml in 4-6 hrs")

xdh3()

#input("Please press `Enter' to exit.")
