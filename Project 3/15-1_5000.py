import matplotlib.pyplot as plt

# Define data.
x_values = list(range(5001))
cubes = [x**3 for x in x_values]

# Make plot.
plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.scatter(x_values, cubes, s=10)

# Set chart title and label axes.
ax.set_title("5000 Cube #", fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Cube of Value', fontsize=14)

# Set size of tick labels, and set range for each axis.
ax.tick_params(axis='both', labelsize=14)
ax.axis([0, 5100, 0, 5100**3])

# Show plot.
plt.savefig('15-1_5000.png', bbox_inches='tight')