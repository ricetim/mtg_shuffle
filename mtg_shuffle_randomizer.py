import random
import numpy as np

deck_size = 60
deck = [0] * deck_size
deck[0] = 100
deck_sum = [0] * deck_size
i = 100000
iterations = i


while(i != 0):
	random.shuffle(deck)
	deck_sum = np.add(deck,deck_sum)
	i = i - 1

print(np.divide(deck_sum,iterations))
# print(np.std(np.divide(deck_sum,iterations)))