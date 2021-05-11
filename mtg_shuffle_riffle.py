import numpy as np
import math

# deck_size = 60
deck = [0] * 60
deck[0] = 100
deck_sum = [0] * 60
num_shuffles = 10
counter = iterations = 100000

def sigmoid(x):
    k = 200
    return 1 / (1 + math.exp(-k*x))

# takes an array (deck) and splits it into two halvs, according to the binomial distribution
def deck_cut(d):
    cut_point = np.random.binomial(len(d),0.5)
    deck_a = d[:cut_point]
    deck_b = d[cut_point:]
    return deck_a,deck_b

# takes in two decks (arrays) and riffle shuffles them together.
def sigmoid_riffle(a,b):
    shuffled_deck = []
    deck_size = len(a) + len(b)
    while(len(shuffled_deck) != deck_size):
        proportion_a = len(a)/(len(a)+len(b))
        proportion_b = len(b)/(len(a)+len(b))
        a_diff = proportion_a - proportion_b
        b_diff = proportion_b - proportion_a
        prob_a = sigmoid(a_diff)
        prob_b = sigmoid(b_diff)
        if np.random.choice([0,1],p=[prob_a,prob_b]):
            shuffled_deck.append(b[0])
            b = b[1:]
        else:
            shuffled_deck.append(a[0])
            a = a[1:]
    return shuffled_deck

# takes in two decks (arrays) and riffle shuffles them together.
def modified_riffle(a,b):
    shuffled_deck = []
    deck_size = len(a) + len(b)
    choose_a = 0
    choose_b = 0
    while(len(shuffled_deck) != deck_size):
        proportion_a = len(a)/(len(a)+len(b))
        proportion_b = len(b)/(len(a)+len(b))
        if proportion_a == 0:
            prob_a = 0
            prob_b = 1
        elif proportion_b == 0:
            prob_a = 1
            prob_b = 0
        elif proportion_a > proportion_b:
            prob_a = 0.9
            prob_b = 0.1
        elif proportion_a <= proportion_b:
            prob_a = 0.1
            prob_b = 0.9
        if np.random.choice([0,1],p=[prob_a,prob_b]):
            shuffled_deck.append(b[0])
            b = b[1:]
        else:
            shuffled_deck.append(a[0])
            a = a[1:]
    return shuffled_deck


# mashes two decks together
def mash_shuffle(a,b):
    shuffled_deck = []
    overlap_point_a = len(a) - np.random.binomial(9,0.5)
    overlap_point_b = np.random.binomial(9,0.5)
    shuffled_deck.extend(b[:overlap_point_b])
    b = b[overlap_point_b:]
    a_end = a[overlap_point_a:]
    a = a[:overlap_point_a]
    while(len(shuffled_deck) != (deck_size - len(a_end))): 
        proportion_a = len(a)/(len(a)+len(b))
        proportion_b = len(b)/(len(a)+len(b))
        a_diff = proportion_
        a - proportion_b
        b_diff = proportion_b - proportion_a
        prob_a = sigmoid(a_diff)
        prob_b = sigmoid(b_diff)
        if np.random.choice([0,1],p=[prob_a,prob_b]):
            shuffled_deck.append(b[0])
            b = b[1:]
        else:
            shuffled_deck.append(a[0])
            a = a[1:]
    shuffled_deck.extend(a_end)
    return shuffled_deck
    
# riffle shuffle more likely to interleave cards
def riffle(a,b):
    shuffled_deck = []
    deck_size = len(a) + len(b)
    while(len(shuffled_deck) != deck_size):
        prob_a = len(a)/(len(a)+len(b))
        prob_b = len(b)/(len(a)+len(b))
        if np.random.choice([0,1],p=[prob_a,prob_b]):
            shuffled_deck.append(b[0])
            b = b[1:]
        else:
            shuffled_deck.append(a[0])
            a = a[1:]
    return shuffled_deck

# performs multiple riffle shuffles
def repeat_riffle(d,i):
    while(i != 0):
        cut_decks = deck_cut(d)
        d = modified_riffle(cut_decks[0],cut_decks[1])
        i = i - 1
    return d

def streak_test(a,b):
    # d = sigmoid_riffle(a,b)
    # d = riffle(a,b)
    d = modified_riffle(a,b)
    print(d)
    i = 1
    s = d[0]
    streak = 1
    streak_array = [0] * 20
    while (i != len(d)):
        if s != d[i]:
            streak_array[streak] = streak_array[streak] + 1
            s = d[i]
            streak = 1
        else:
            streak = streak + 1
        i = i + 1
    streak_array[streak] = streak_array[streak] + 1
    return streak_array


while(counter != 0):
    shuffled_deck = repeat_riffle(deck,num_shuffles)
    deck_sum = np.add(shuffled_deck,deck_sum)
    counter = counter - 1

# print(streak_test([0]*100,[1]*100))

#print(sigmoid_riffle([0]*30,[1]*30))
#print(mash_shuffle([0]*30,[1]*30))
#determine the average value of each position in the deck
print(np.divide(deck_sum,iterations))
# check the standard deviations of the deck positions
# print(np.std(np.divide(deck_sum,iterations)))