import csv
question = 'y'
loop = 0
test_limit_total = 0
total_average = 0
total_j = 0
odds = input('seached odds?')
#scope = input('How many seasons? Max 13.')
#scope = int(scope)
scope = 13
result = input('H, A or D?')
average_odds = 0
if result == 'H':
	odds_column = 22
elif result == 'D':
	odds_column = 23
else:
	odds_column = 24
list_number = 0
filename_list = ['19', '18', '17', '16', '15', '14', '13', '12', '11', '10', '09', '08', '07']
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
		tested_other_cell = exampledata[i][6]
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
	if total_j > 50:
		break
	else:
		continue
total_average = total_average / loop
total_average = round(total_average,2)
percentage_chance = 100 / total_average
percentage_chance = round(percentage_chance,2)
print('Total found: ' + str(total_j))
print('Total average:' + str(total_average))
print('Percentage chance:' + str(percentage_chance) + "%")
print('Games checked: ' + str(test_limit_total))
odds_file = open('list.txt', 'a')
odds_file.write(str(result) + ' Odds: ' + str(odds) + ' True: ' + str(total_average) + ' Percentage: ' + str(percentage_chance) + '\n')
odds_file.close()

