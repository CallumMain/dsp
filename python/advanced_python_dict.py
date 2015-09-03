import csv

def nameDict(data):
	d = {}
	for dt in data:
		name = dt[0].split()[-1]
		if name in d:
			d.get(name).append(dt[1:])
		else:
			d[name] = dt[1:]

	return d

def tupleDict(data):
	d = {}
	for dt in data:
		name = dt[0].split()
		t = tuple([name[0], name[-1]])
		if t in d:
			d.get(t).append(dt[1:])
		else:
			d[t] = dt[1:]

	return d

def lastDict(data):
	d = {}
	for dt in data:
		name = dt[0].split()
		t = tuple([name[-1], name[0]])
		if t in d:
			d.get(t).append(dt[1:])
		else:
			d[t] = dt[1:]

	return d

with open('faculty.csv', 'rb') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		parsed_data = list(reader)

d = lastDict(parsed_data)
for key in sorted(d):
  item = d.popitem()
  print item
