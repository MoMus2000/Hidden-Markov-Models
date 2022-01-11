import numpy as np
import csv


file = open("/Users/a./Desktop/markov/hmm_class/site_data.csv")
file = csv.reader(file)
rows = []
# print(type(file))
# print(file)
transitions = {}

total_sum = {}

for row in file:
	l = row[0]
	r = row[1]

	if (l, r) not in transitions:
		transitions[(l, r)] = 0
	else:
		transitions[(l, r)] += 1

	if l not in total_sum:
		total_sum[l] = 0
	else:
		total_sum[l] += 1

# Calculating Probabilities

for k, v in transitions.items():
	l, r = k
	transitions[k] = v/total_sum[l]

best_page = -1
ind = -1
for k,v in transitions.items():
	l, r = k
	if l == "-1":
		if transitions[(l, r)] > best_page:
			best_page = transitions[(l, r)]
			ind = r

		print(transitions[(l, r)])


print("Highest Landing is rate is index: ", ind, best_page)


bounce_page = -1
ind = -1
for k,v in transitions.items():
	l, r = k
	if r == "B":
		if transitions[(l, r)] > bounce_page:
			bounce_page = transitions[(l, r)]
			ind = l

		print(transitions[(l, r)])

print("Highest Bounce rate is index: ", ind, bounce_page)

# print(transitions)
# print(total_sum)