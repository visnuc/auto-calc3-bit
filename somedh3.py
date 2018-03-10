from message3 import message3

def somedh3():
  wt = float(input("Weight (kg): "))
  sam = str(input("SAM-SUW / Non-SAM [1/2]: "))
  if sam == "1":
    print("\n", wt*10, "ml/hr for 2 hrs, \
then\n", wt*5, "ml/hr for 8-10 hrs (GORS)\n")
  elif sam == "2": 
    print("\n", wt*75, "ml over 4-6 hrs (GORS)\n")
  else:
    print(" \nPlease try again.")

somedh3()
#input("Press `Enter' to exit.")
