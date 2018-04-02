friends = []
friends_id = []
friends_friends = []
friends_friends_id = []
fr_fr_id = []

with open('beCoder_input.txt', 'r') as f:
	n = int(f.readline(1))
	f.readline(1)
	for i in range(n):
		friends.append(f.readline())

for i in range(len(friends)):
	friends_id.append(friends[i][0:4])
	for k in range(int(friends[i][5])):
		friends_friends_id.append(friends[i].split()[2+k])

for i in friends_friends_id:
	if not any(i in s for s in friends_id):
		fr_fr_id.append(i)

n = len(set(fr_fr_id))
print(n)
