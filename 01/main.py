from itertools import groupby
import numpy as np

# Count the calories per elf
elf_calories = []

with open('input') as f_data:
    for k, g in groupby(f_data, lambda x: x.startswith('\n')):
        if not k:
            elf_calories.append(
                    np.array(
                        [[int(x) for x in d.split()] for d in g if len(d.strip())]
                    ).sum()
                )

# Top elf
# print(np.max(elf_calories), np.argmax(elf_calories)+1)
print(f"Q1: Top elf calories: {np.max(elf_calories)}")

# Top 3 elves
top_3 = np.sort(elf_calories)[-3:]
# print(top_3)
print(f"Q2: Sum of top 3 elves calories: {top_3.sum()}")
