# Eibhinn Lee
# plot f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4]

# Import our modules
import matplotlib.pyplot as plt
import numpy as np

# Create the vectors X, G,and H
x = np.array(range(4))
g = x ** 2
h = x ** 3

# Create the plot
plt.plot(x,y)
plt.plot(x,h)

# Show the plot
plt.show()











