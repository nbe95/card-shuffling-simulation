import sys
import random


def shuffle_ideal(deck):
    return random.sample(deck, len(deck))


def shuffle_overhand(deck, fw_only):
    size = len(deck)
    steps = 6
    cards_min = 1
    cards_max = int(size / 3)
    for _ in range(steps):
        deck_new = []
        while len(deck) > 0:
            cards = min(len(deck), random.randint(cards_min, cards_max))
            if fw_only or random.random() >= 0.5: # fw
                deck_new = deck[:cards] + deck_new
            else: # bw
                deck_new = deck_new + deck[:cards]
            deck = deck[cards:]
        deck = deck_new
    return deck


def shuffle_overhand_fw(deck):
    return shuffle_overhand(deck, True)


def shuffle_overhand_fwbw(deck):
    return shuffle_overhand(deck, False)


def getRandomness(deck):
    size = len(deck)
    deck = deck[:] + [deck[0]]
    count = 0
    for i in range(size):
        #if deck[i] + 1 == deck[i + 1] or deck[i] + 1 - size == deck[i + 1] or deck[i] + 1 == deck[i + 1] - size:
        if abs(deck[i] - deck[i + 1]) == 1 or abs(deck[i] - deck[i + 1]) == size - 1:
            count += 1
    return 1 - (count / size)


def main(iterations, cards_total):
    methods     = [shuffle_ideal, shuffle_overhand_fw, shuffle_overhand_fwbw]

    print("Testing the randomness of a total of %d cards using %d different shuffling methods and %d simulation iterations." % (cards_total, len(methods), iterations))
    print("In order to determine the randomness of a shuffled card deck, any former neighbor cards still lying next to each other after shuffling are counted. This number of cards is simply compared to the total deck size.\n")

    cards_shuffled  = [0] * len(methods)
    rand_iter       = [0] * len(methods)
    total_sum       = [0] * len(methods)

    for i in range(iterations):
        out = "%d:\t" % (i + 1)

        cards = list(range(0, cards_total))
        for m in range(len(methods)):
            cards_shuffled[m] = methods[m](cards)
            rand_iter[m] = getRandomness(cards_shuffled[m])
            total_sum[m] += rand_iter[m]
            out += "%3.2f%%\t\t" % (rand_iter[m] * 100)

        print(out)

    print("-" * 60)
    for m in range(len(methods)):
        print("Average randomness for shuffling method %d '%s': %3.2f%%" % (m + 1, methods[m].__name__, (total_sum[m] / iterations) * 100))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:\n\t%s [<ITERATIONS> [<NUMBER OF CARDS>]]\n" % __file__)

    iterations = 50
    if len(sys.argv) >= 2:
        iterations = int(sys.argv[1])

    cards = 52
    if len(sys.argv) >= 3:
        cards = int(sys.argv[2])

    main(iterations, cards)