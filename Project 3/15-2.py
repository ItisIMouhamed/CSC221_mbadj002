import matplotlib.pyplot as plt

# Define data.
x_values = [1, 2, 3, 4, 5]
y_values = [1, 8, 27, 64, 125]

# Make plot.
plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=40) #15-2

# Set chart title and label axes.
ax.set_title("Cube", fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Cube of Value', fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', labelsize=14)

# Show plot.
plt.savefig('cube_plot.png', bbox_inches='tight')



# Plotting the first 5,000 cubic numbers
x_values = list(range(5001))
y_values = [x**3 for x in x_values]


plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=40) #15-2

# Set chart title and label axes.
ax.set_title("First 5000 Cubic #", fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Cube of Value', fontsize=14)

# Set size of tick labels, and set range for each axis.
ax.tick_params(axis='both', labelsize=14)
ax.axis([0, 5100, 0, 5100**3])

# Show plot.
plt.savefig('5000cube_plot.png', bbox_inches='tight')

