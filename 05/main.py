import re

with open("input", "r") as f:
    data = f.readlines()
    raw_stacks = data[:8]
    raw_move = data[10:]

moves_list = [re.split("move | from | to ", m.strip("\n"))[1:] for m in raw_move]

# stack = [re.split("[|] [|]", s.strip("\n")) for s in raw_stacks]
stack = [s.strip("\n") for s in raw_stacks]
# flip up/down
stack = stack[::-1]

def get_stack(stack) -> dict:
    stack_dict = {}
    for s in range(9):  # go over stacks
        stack_dict[s+1] = []
        for c in range(8):  # go over crates
            # print(s, c, stack[c][4*s+1])
            crate = stack[c][4*s+1]
            if crate != " ":
                stack_dict[s+1] += crate
    return stack_dict

# print(stack_dict)

# Q1: Crates are moved one by one
# Run moves
stack_dict = get_stack(stack)
for items, source, target in moves_list:
    items, source, target = int(items), int(source), int(target)
    # print(items, source, target)
    for _ in range(items):
        # print(f"pre-pick")
        # print(stack_dict)
        # pick up crate
        crate = stack_dict[source].pop()
        # print(f"picked up crate {crate}")
        # drop to new location
        stack_dict[target] += crate
        # print(f"post-pick")
        # print(stack_dict)

last_layer = "".join([s.pop() for s in stack_dict.values()])
print(f"{last_layer = }")

# Q2: Crates are moved all at a time
# Run moves
stack_dict = get_stack(stack)
# i = 0
for items, source, target in moves_list:
    items, source, target = int(items), int(source), int(target)

    print(items, source, target)
    print(f"pre-pick")
    print(stack_dict)
    # pick up crate
    crates = stack_dict[source][-items:]
    del stack_dict[source][-items:]
    print(f"picked up {crates = }")
    # drop to new location
    stack_dict[target] += crates
    print(f"post-pick")
    print(stack_dict)
    # if i > 2:
    #     break
    # i+=1
print(stack_dict)
last_layer = "".join([s.pop() for s in stack_dict.values()])
print(f"{last_layer = }")
