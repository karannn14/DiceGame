import random
import pyfiglet
banner = pyfiglet.figlet_format("Dice!!")
print(banner)
try:
  print(int(input("Enter Min_value:")))
  print(int(input("Enter Maxvalue:")))
  min_value = 1
  max_value = 6
except:
  invalid = pyfiglet.figlet_format("Invalid!")
  print(invalid)

again = True

while again:
  print(random.randint(min_value,max_value))
  again_roll = input("Wanna Roll Again (yes/no):")
  if again_roll.lower() == 'yes' or again_roll.lower() == 'y':
    continue
  else:
    break
