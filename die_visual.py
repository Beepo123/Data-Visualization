from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

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

# Visualize the results.
x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling one D6 1,000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')