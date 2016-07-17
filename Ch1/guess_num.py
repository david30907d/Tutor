import random as r
try:
	upperBound = int(input("Please input an UpperBound :"), 10)
	lowerBound = int(input("Please input an lowerBound :"), 10)
	ans = r.randint(lowerBound, upperBound)

	while True:
		user = input("input the num you guessed :")
		if int(user) == ans:
			print("Congrtulaitons !")
			break

except Exception as e:
	print(e)
	raise e
