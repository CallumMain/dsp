import csv

def nameDict(data):
	d = {}
	for dt in data:
		name = dt[0].split()[-1]
		if name in d:
			d.get(name).append(dt[1:])
		else:
			d[name] = dt[1:]

	for key in sorted(d):
  		item = d.popitem()
  		print item

def tupleDict(data):
	d = {}
	for dt in data:
		name = dt[0].split()
		t = tuple([name[0], name[-1]])
		if t in d:
			d.get(t).append(dt[1:])
		else:
			d[t] = dt[1:]

	for key in sorted(d):
  		item = d.popitem()
  		print item

def lastDict(data):
	d = {}
	for dt in data:
		name = dt[0].split()
		t = tuple([name[0], name[-1]])
		if t in d:
			d.get(t).append(dt[1:])
		else:
			d[t] = dt[1:]
	sorted_items = sorted(d.items(), key=lambda (k, v): (k[1], k[0]))
	print sorted_items[:3]

with open('faculty.csv', 'rb') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		parsed_data = list(reader)

nameDict(parsed_data)
tupleDict(parsed_data)
lastDict(parsed_data)
