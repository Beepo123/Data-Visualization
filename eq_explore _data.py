import json

# Explore the structure of the data
filename = "data/eq_data_1_day_m1.json"
with open(filename, encoding="utf8") as file:
    all_eq_data = json.load(file)

all_eq_dicts = all_eq_data['features']
mags, locs = [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    loc = eq_dict['properties']['place']
    mags.append(mag)
    locs.append(loc)

for i in range(10):
    print(f"Place: {locs[i]}\nMagnitude: {mags[i]}\n")