import re

with open("input", "r") as f:
    # raw_data = f.readlines(200)
    raw_data = f.readlines()

print(raw_data)

data = [
    re.split(",|-", d.strip("\n")) for d in raw_data
]


# Q1
complete_overlap_total = 0

for a1_start, a1_end, a2_start, a2_end in data:
    # print(a1_start)
    # print(a1_end)
    # print(a2_start)
    # print(a2_end)
    a1_start = int(a1_start)
    a1_end = int(a1_end)
    a2_start = int(a2_start)
    a2_end = int(a2_end)

    # a1 fully contained in a2
    if (a1_start >= a2_start) and (a1_end <= a2_end):
        # print(f"Overlap case 1! {a1_start}-{a1_end} contained in {a2_start}-{a2_end}")
        complete_overlap_total += 1

    # a2 fully contained in a1
    elif (a1_start <= a2_start) and (a1_end >= a2_end):
        # print(f"Overlap case 2! {a2_start}-{a2_end} contained in {a1_start}-{a1_end}")
        complete_overlap_total += 1

print(f"{complete_overlap_total = }")


# Q2
partial_overlap_total = 0

for a1_start, a1_end, a2_start, a2_end in data:
    a1_start = int(a1_start)
    a1_end = int(a1_end)
    a2_start = int(a2_start)
    a2_end = int(a2_end)
    print(f"{a1_start}-{a1_end} {a2_start}-{a2_end}")

    # a1 overalps a2 start
    if (a1_start <= a2_start) and (a2_start <= a1_end):
        print(f"Partial overlap case 1! {a1_start}-{a2_start}-{a1_end}")
        partial_overlap_total += 1

    # a1 overlaps a2 end
    elif (a1_start <= a2_end) and (a2_end <= a1_end):
        print(f"Partial overlap case 2! {a1_start}-{a2_end}-{a1_end}")
        partial_overlap_total += 1

    # a2 overalps a1 start
    elif (a2_start <= a1_start) and (a1_start <= a2_end):
        print(f"Partial overlap case 3! {a2_start}-{a1_start}-{a2_end}")
        partial_overlap_total += 1

    # a2 overlaps a1 end
    elif (a2_start <= a1_end) and (a1_end <= a2_end):
        print(f"Partial overlap case 4! {a2_start}-{a1-end}-{a2_end}")
        partial_overlap_total += 1

print(f"{partial_overlap_total = }")
