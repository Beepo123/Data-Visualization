from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

# Create two D6
die_1 = Die()
die_2 = Die()

# make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# count the number of occourances of each side
# and store it in a list
max_result = die_1.num_sides + die_2.num_sides
frequencies = list(range(0,max_result))
for value in results:
    frequencies[value-1] += 1

# Visualize the results.
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling two D6 dice 1000 times',
xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')