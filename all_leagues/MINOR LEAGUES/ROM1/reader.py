import csv
question = 'y'
loop = 0
test_limit_total = 0
total_average = 0
total_j = 0
odds = input('seached odds?')
scope = 1
result = input('H, A or D?')
average_odds = 0
if result == 'H':
	odds_column = 16
elif result == 'D':
	odds_column = 17
else:
	odds_column = 18
list_number = 0
filename_list = ['ROM']
while list_number < scope:
	filename = filename_list[list_number]
	filename = filename + ".csv"
	odds_column = int(odds_column)
	examplefile = open(filename)
	examplereader = csv.reader(examplefile)
	exampledata = list(examplereader)
	test_limit = len(list(csv.reader(open(filename))))
	test_limit_total += test_limit
	i = 1
	j = 0
	successes = 0
	while i < int(test_limit):
		tested_cell = exampledata[i][odds_column]
		tested_other_cell = exampledata[i][9]
		if odds in tested_cell:
			j+=1
			i+=1		
			if result in tested_other_cell:
				successes+=1
				average_odds += float(tested_cell)
			else:
				average_odds += float(tested_cell)
				continue
		else:
			i+=1
	print('Found: ' + str(j))
	print('Successes: ' + str(successes))
	print('Average odds: ' + str(average_odds))
	if j == 0 and successes == 0:
		print("no samples")
	elif j > 0 and successes == 0:
		average = 0
		print(average)
		loop += 1
		total_average += average
	else:
		average = j / successes
		print(average)
		loop += 1
		total_average += average
	total_j += j
	list_number += 1
total_average = total_average / loop
percentage_chance = 100 / total_average
print('Total found: ' + str(total_j))
print('Total average:' + str(total_average))
print('Percentage chance:' + str(percentage_chance) + "%")
print('Games checked: ' + str(test_limit_total))

