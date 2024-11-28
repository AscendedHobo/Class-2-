def count_vowels(string):
	# implement code here to count vowels
	vowels = ["a", "e", "i", "o", "u"]
	count = 0
	for i in range(0, len(string)):
		if string[i] in vowels:
			count += 1
		
	return count

print(count_vowels("for real"))

