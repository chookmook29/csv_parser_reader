import csv
question = 'y'
loop = 0
total_average = 0
odds = input('seached odds?')
while question != 'n':
	filename = input('your filename?')
	odds_column = input('which odds column?')
	odds_column = int(odds_column)
	examplefile = open(filename)
	examplereader = csv.reader(examplefile)
	exampledata = list(examplereader)
	test_limit = test_limit = len(list(csv.reader(open(filename))))
	i = 1
	j = 0
	successes = 0
	while i < int(test_limit):
		tested_cell = exampledata[i][odds_column]
		tested_other_cell = exampledata[i][6]
		if odds in tested_cell:
			j+=1
			i+=1		
			if 'H' in tested_other_cell:
				successes+=1
			else:
				continue
		else:
			i+=1
	print(j)
	print('Successes: ' + str(successes))
	average = j / successes
	print(average)
	loop += 1
	total_average += average
	question = input('Continue?')
	if question == "n":
		total_average = total_average / loop
		percentage_chance = 100 / total_average
		print('Total average:' + str(total_average))
		print('Percentage chance:' + str(percentage_chance) + "%")

