data = []
sum_len = 0
with open('reviews.txt', 'r') as r:
	for line in r:
		sum_len += len(line)
		data.append(line)
print('Here are ',len(data),'commits.')
print('The total length is',sum_len)
# print(data[0])
# print('Averange length of data is', sum_len / len(data))

wc = {}
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1 #查找並增加
		else:
			wc[word] = 1 #新增KEY
# for word in wc:
# 	if wc[word] > 1000:
# 		print(word, wc[word])

while  True:
	word = input('Please enter the keyword ')
	if word == 'q':
		print('Thank you')
		break
	if word in wc:
		print('We use ', word,wc[word],' times')
	else:
		print('We can not find the word')
	
# new = []
# for d in data:
# 	if len(d) < 100:
# 		new.append(d)
# print('There are', len(new),'commits shortert than 100 bytes.')
# print(new[0])

# keyword = []
# for d in data:
# 	if 'good' in d:
# 		if 'great' in d:
# 			keyword.append(d)
# print('There are', len(keyword),'commits mentioned the word"good".')
# print(keyword[0])

# keyword = [d for d in data if 'good' in d]
# print(len(keyword)[0])
