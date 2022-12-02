import pandas as pd

data = pd.read_csv("input", header=None, delimiter=" ")
print(data.head())

selection_dict = {"X": 1, "Y": 2, "Z": 3}


selection = data[1].replace(selection_dict)
print(selection)
