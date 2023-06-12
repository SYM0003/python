import os
choice = int(input("shutdown your computer? (y or n)"))

#if choice == "y" or choice == "Y":
if choice == 1:
    os.system("shutdown /s /t 0")
else:
              print("Exiting the program")
