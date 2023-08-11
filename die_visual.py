from die import Die

# Create a D6
die = Die()

# make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    results.append(die.roll())

# count the number of occourances of each side
# and store it in a list
frequencies = [0, 0, 0, 0, 0, 0]
for value in results:
    frequencies[value-1] += 1

for count, value in enumerate(frequencies):
    print(f"count: {count+1}, frequency: {value}")
