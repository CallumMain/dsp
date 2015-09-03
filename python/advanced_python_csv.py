import re, csv
def email(data):
	EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")
	emails = []
	for line in data:
		for s in line:
			emails.extend(re.findall(EMAIL_REGEX, s))

	return emails

with open('faculty.csv', 'rb') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		parsed_data = list(reader)

emails = email(parsed_data)

writer = csv.writer(open('emails.csv', 'wb'))
for e in emails:
	writer.writerow([e])
