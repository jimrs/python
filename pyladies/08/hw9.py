def romanToInt(roman):
	romanNumerals = {
		"I": 1,
		"V": 5,
		"X": 10
	}

	romanList = list(roman)
	result = 0
	previousPopValue = 0

	while len(romanList) > 0:

		char = romanList.pop()

		for numeral, value in romanNumerals.items():
			if char == numeral:

				if value < previousPopValue:
					result -= value
					previousPopValue = value

				else:
					result += value
					previousPopValue = value			

	return result


'''
top down
1. take string and trasform to integer
2. pop a char and assign a numerical value to it
3. add this numerical value to result
4. get I, II, III working
5. get IV working
	if the popped char is of smaller value than the previous pop,
		do a difference instead of a sum
'''