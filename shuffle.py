"""Card shuffling simulation module."""

from random import randint, random, sample
from sys import argv
from typing import Callable, List, Tuple


def shuffle_ideal(deck: List[int]) -> List[int]:
    """Get a nearly ideally shuffled deck."""
    return sample(deck, len(deck))


def shuffle_overhand(deck: List[int], fw_only: bool) -> List[int]:
    """Return a deck shuffled by the overhand method."""
    steps: int = 6
    cards_min: int = 1
    cards_max: int = int(len(deck) / 3)
    for _ in range(steps):
        deck_new: List[int] = []
        while len(deck) > 0:
            cards: int = min(len(deck), randint(cards_min, cards_max))
            if fw_only or random() >= 0.5:  # forward
                deck_new = deck[:cards] + deck_new
            else:  # backward
                deck_new = deck_new + deck[:cards]
            deck = deck[cards:]
        deck = deck_new
    return deck


def shuffle_overhand_fw(deck: List[int]) -> List[int]:
    """Return an overhand-shuffled deck using only forward shuffles."""
    return shuffle_overhand(deck, True)


def shuffle_overhand_fw_bw(deck: List[int]) -> List[int]:
    """Return an overhand-shuffled deck using both fwd. and bwd. shuffles."""
    return shuffle_overhand(deck, False)


def get_randomness(deck: List[int]) -> float:
    """Determine how much randomized a given card deck is."""
    size: int = len(deck)
    deck = deck[:] + [deck[0]]
    count: int = 0
    for i in range(size):
        if (
            abs(deck[i] - deck[i + 1]) == 1
            or abs(deck[i] - deck[i + 1]) == size - 1
        ):
            count += 1
    return 1 - (count / size)


def main(iterations: int, cards_total: int) -> None:
    """Run simulation."""
    methods_to_check: Tuple[Callable[[List[int]], List[int]], ...] = (
        shuffle_ideal,
        shuffle_overhand_fw,
        shuffle_overhand_fw_bw,
    )

    print(
        f"Testing the randomness of a total of {cards_total} cards using "
        f"{len(methods_to_check)} different shuffling methods and "
        f"{iterations} simulation iterations."
    )

    cards_shuffled: List[List[int]] = [[]] * len(methods_to_check)
    rand_iter: List[float] = [0] * len(methods_to_check)
    total_sum: List[float] = [0] * len(methods_to_check)

    for i in range(iterations):
        out = f"{i + 1}:\t"

        cards: List[int] = list(range(0, cards_total))
        for m, method in enumerate(methods_to_check):
            cards_shuffled[m] = method(cards)
            rand_iter[m] = get_randomness(cards_shuffled[m])
            total_sum[m] += rand_iter[m]
            out += f"{rand_iter[m] * 100:3.2f}%\t\t"
        print(out)

    print("-" * 60)
    for m, method in enumerate(methods_to_check):
        print(
            f"Average randomness for shuffling method {m + 1} "
            f"'{method.__name__}': {total_sum[m] / iterations * 100:3.2f}%"
        )


if __name__ == "__main__":
    if len(argv) < 2:
        print(f"Usage:\n\t{__file__} [<ITERATIONS> [<NUMBER OF CARDS>]]\n")

    arg_iterations: int = int(argv[1]) if len(argv) >= 2 else 50
    arg_cards_total: int = int(argv[2]) if len(argv) >= 3 else 52
    main(arg_iterations, arg_cards_total)
