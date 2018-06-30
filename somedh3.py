from message3 import message3

def somedh3():
  wt = float(input("Weight (kg): "))
  sam = str(input("SAM-SUW(1)/ Non-SAM(2) ?\nEnter code: "))
  if sam == "1":
    print("\n", round(wt*10, 2), "ml/hr for 2 hrs, \
then\n", round(wt*5, 2), "ml/hr for 8-10 hrs (GORS)\n")
  elif sam == "2":
    print("\n", round(wt*75, 2), "ml over 4-6 hrs (GORS)\n")
  else:
    print(" \nPlease try again.")

somedh3()
#input("Press `Enter' to exit.")
