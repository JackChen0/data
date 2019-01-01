data = []
sum_len = 0
with open('reviews.txt', 'r') as r:
	for line in r:
		sum_len += len(line)
		data.append(line)
print('Here are ',len(data),'commits.')
print('The total length is',sum_len)
print('Averange length of data is', sum_len / len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('There are', len(new),'commits shortert than 100 bytes.')
print(new[0])
