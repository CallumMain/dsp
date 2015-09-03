import re, csv

def degrees(data):
	d = []
	for line in data:
		degree = line[1].split()
		for dg in degree:
			l = re.sub(r'\.', '', dg)
			d.append(l)

	d.sort()
	dt = {x:d.count(x) for x in d}
	a,b = dt.keys(), dt.values()

	print a,b

def titles(data):
	TITLE_REGEX = re.compile(r"\Professor\b")
	title = []
	for line in data:
		for s in line:
			if TITLE_REGEX.search(s) is not None:
				title.append(s)

	title.sort()
	d = {x:title.count(x) for x in title}
	a,b = d.keys(), d.values()

	print a,b

def email(data):
	EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")
	emails = []
	for line in data:
		for s in line:
			emails.extend(re.findall(EMAIL_REGEX, s))

	print emails

def domains(data):
	unique = set()
	for line in data:
		for s in line:
			domain = re.search("@[\w.]+", s)
			if domain != None:
				unique.add(domain.group())

	print list(unique)


with open('faculty.csv', 'rb') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		parsed_data = list(reader)

titles(parsed_data)
