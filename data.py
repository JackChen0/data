data = []
sum_len = 0
with open('reviews.txt', 'r') as r:
	for line in r:
		sum_len += len(line)
		data.append(line)
print('Here are ',len(data),'commits.')
print('The total length is',sum_len)
print('Averange length of data is', sum_len / len(data))
