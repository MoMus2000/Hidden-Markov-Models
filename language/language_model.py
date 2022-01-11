import numpy as np
import string

file = open('/Users/a./Desktop/markov/test/jane.txt')

initial = {}

second_word = {}

transitions = {}


def remove_punc(s):
	return s.translate(str.maketrans('', '', string.punctuation)).rstrip().lower()

def add_to_dict(d, k, v):
	if k not in d:
		d[k] = []
	d[k].append(v)
	return d

# ["DOG", "DOG", "CAT"]
def list_to_prob(arr):
	hash_map = {}
	total_items = len(arr)
	for item in arr:
		if item in hash_map:
			hash_map[item] += 1
		else:
			hash_map[item] = 1

	for key, v in hash_map.items():
		hash_map[key] = v/total_items

	return hash_map

def sample_word(hash_map):
	po = np.random.random()
	cumulative = 0 

	for k, v in hash_map.items():
		cumulative += v
		if po < cumulative:
			return k

	assert(False)

def main():
	for row in file:
		tokenized = remove_punc(row).split()

		T = len(tokenized)

		for i in range(0, T):
			
			token = tokenized[i]
			
			if i == 0:
				if token not in initial:
					initial[token] = 1
				else:
					initial[token] += 1
			else:
				prev_token = tokenized[i-1]

				if i == T-1:
					add_to_dict(transitions, (prev_token, token), "END")

				if i == 1:
					add_to_dict(second_word, prev_token, token)

				else:
					prev_token_1 = tokenized[i-2]
					add_to_dict(transitions, (prev_token_1, prev_token), token)

	# Normalize the distribution

	total = sum(initial.values())
	for k, v in initial.items():
		initial[k] = v/total

	# print(initial)

	for t_1, t in second_word.items():
		second_word[t_1] = list_to_prob(t)

	for k, ts in transitions.items():
		transitions[k] = list_to_prob(ts)



	#generate

	for i in range(10):
		sentence = []
		w0 = sample_word(initial)
		sentence.append(w0)
		w1 = sample_word(second_word[w0])
		sentence.append(w1)

		while(1):
			w2 = sample_word(transitions[(w0, w1)])
			if w2 == "END":
				break
			sentence.append(w2)
			w0 = w1
			w1 = w2

		print(' '.join(sentence))




if __name__ == "__main__":
	main()

	# total = 0
	# counter = {"DOG":0, "CAT":0}
	# for i in range(0, 100000):
		# counter[sample_word(hash_map)] += 1

	# print("DOG", counter["DOG"]/100000)
	# print("CAT", counter["CAT"]/100000)