import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data
filename = "data/eq_data_1_day_m1.json"
with open(filename, encoding="utf8") as file:
    all_eq_data = json.load(file)

# Get magnitues and locations and store in list
all_eq_dicts = all_eq_data["features"]
mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict["properties"]["mag"])
    lons.append(eq_dict["geometry"]["coordinates"][0])
    lats.append(eq_dict["geometry"]["coordinates"][1])
    hover_texts.append(eq_dict["properties"]["title"])

# Map the earthquake
data = [
    {
        "type": "scattergeo",
        "lon": lons,
        "lat": lats,
        "text": hover_texts,
        "marker": {
            "size": [abs(5 * mag) for mag in mags],
            "color": mags,
            "colorscale": "Viridis",
            "reversescale": True,
            "colorbar": {"title": "Magnitude"},
        },
    }
]

# Plot the result
layout_title = all_eq_data["metadata"]["title"]
my_layout = Layout(title=layout_title)
fig = {"data": data, "layout": my_layout}
offline.plot(fig, filename="global_earthquake.html")
