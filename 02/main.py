import pandas as pd

data = pd.read_csv("input", dtype="str", header=None)

# ABC: rock/paper/scissor opponent
# XYZ: rock/paper/scissor you
# win=6, tie=3, loss=0
# select 1/2/3 rock/paper/scissor
selection_dict = {
    "A X": 1,
    "A Y": 2,
    "A Z": 3,
    "B X": 1,
    "B Y": 2,
    "B Z": 3,
    "C X": 1,
    "C Y": 2,
    "C Z": 3,
}

payoff_dict = {
    "A X": 3,
    "A Y": 6,
    "A Z": 0,
    "B X": 0,
    "B Y": 3,
    "B Z": 6,
    "C X": 6,
    "C Y": 0,
    "C Z": 3,
}

selection = data[0].replace(selection_dict)
payoff = data[0].replace(payoff_dict)

print(data.head())
print(selection.head())
print(payoff.head())

# Part 1
print(f"{selection.sum() = }")
print(f"{payoff.sum() = }")
print(f"{payoff.sum() + selection.sum() = }")


# Part 2
# XYZ == u must lose, draw, win
strategy_dict = {
    "A X": 0+3,  # rock and lose(0) == play scissor(3)
    "A Y": 3+1,  # rock and draw(3) == play rock(1)
    "A Z": 6+2,
    "B X": 0+1,  # paper
    "B Y": 3+2,
    "B Z": 6+3,
    "C X": 0+2,  #  scissor
    "C Y": 3+3,
    "C Z": 6+1,
}

strategy = data[0].replace(strategy_dict)
print(f"{strategy.sum() = }")
