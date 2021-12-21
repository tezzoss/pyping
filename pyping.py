import os, random
os.system("title %random% %date% %username% %time% %random%")

random = random.randint(1, 9)
os.system(f"color {random}")
def y():
	IP = input("Enter an IP to ping: ")
	os.system(f"ping {IP} -t")
def n():
	IP = input("Enter an IP to ping: ")
	os.system(f"ping {IP} -n 20")
def clear():
	os.system("cls")

clear()
yorn = input("Would you like to ping infinitely? y or n: ")
if yorn == "y":
	clear()
	os.system(f"color {random}")
	y()
else:
	clear()
	os.system(f"color {random}")
	n()