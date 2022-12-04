import string

alphabet = string.ascii_letters
# print(alphabet)
priority_dict = {letter:value+1 for value, letter in enumerate(alphabet)}
# print(priority_dict)

with open("input", "r") as f:
    # data = f.readlines(200)
    data = f.readlines()

priority_value = 0

for compartment in data:
    compartment = compartment.strip("\n")
    cl = len(compartment)
    # print(cl, compartment)
    # print(compartment[:int(cl/2)])
     #print(compartment[int(cl/2):])
    cleft = compartment[:int(cl/2)]
    cright = compartment[int(cl/2):]

    for entry in cleft:
        if entry in cright:
            # print(f"priority: {entry}")
            priority_value += priority_dict[entry]
            break

# Q1
print(f"{priority_value = }")

# Q2
group_value = 0

for idx in range(0, len(data), 3):
    c1 = data[idx+0].strip("\n")
    c2 = data[idx+1].strip("\n")
    c3 = data[idx+2].strip("\n")

    for entry in c1:
        if (entry in c2) and (entry in c3):
            # print(f"group badge: {entry}")
            group_value += priority_dict[entry]
            break
print(f"{group_value = }")
