# Card Shuffling Simulation

One of my very early coding exercises in Python.

## Objective

**Which card shuffling method produces the most randomized card deck?**

In particular: When performing an [overhand
shuffle](https://en.wikipedia.org/wiki/Shuffling#Overhand), does it increase the
total randomness if you put a bunch of cards alternately behind and in front of
the stack?

> :bulb: In order to determine the randomness of a shuffled card deck, any
former neighbor cards still lying next to each other after shuffling are
counted. This number of cards is simply compared to the total deck size.

## Usage

Just run the `shuffle.py` script.

```sh
python -m venv venv
source ./venv/bin/activate

python shuffle.py

```
