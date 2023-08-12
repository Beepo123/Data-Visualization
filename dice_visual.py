from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline
import time

start_time = time.time()

# Create two D6
die_1 = Die(6)
die_2 = Die(6)

# make some rolls, and store results in a list.
results = [die_1.roll() + die_2.roll() for _ in range(1_000_000)]

# count the number of occourances of each side
# and store it in a list
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(1, max_result+1)]

# Visualize the results.
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling D6 and a D10 dice 1000 times',
xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d10.html')

end_time = time.time()

print(f"elapsed time: {end_time-start_time}")