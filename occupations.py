import random, csv

data = {}

def open_da_file(fileName):
	with open(fileName, "r") as infile:
		reader = csv.reader(infile)
		for row in reader:
			k = row[0]
			if k != "Job Class" and k != "Total":
				v = float(row[1])
				data[k] = v
	return data
				
def get_random_occupation(fileName):
	open_da_file(fileName)
	occNum = random.random() * 99.8
	for key in data:
		if occNum - data[key] > 0:
			occNum = occNum - data[key]
		else:
			return key
	

print get_random_occupation("occupations.csv")