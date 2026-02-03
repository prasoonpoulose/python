import os
print ("Hello world")
print(os.getenv("HOSTNAME")) # env variable

if os.getenv("Hostname") == "DELL-LAPTOP":  # Conditional Statement
   print("Its your Laptop")
else:
   print("Oh..Its not your laptop")

