num=10
to_guess=True
while to_guess:
	guess=int(input("guess the number:"))
	if guess==num:
		print("you guessed it right")
		to_guess=False
	elif guess<num:
		print("your guess is lesser than secret number")
	else:
		print("your guess is larger than secret number")