# import random
# from itertools import count
# import pandas as pd
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation


# plt.style.use('fivethirtyeight')

# x_vals = []
# y_vals = []

# index = count()

# def animate(i):
#     x_vals.append(next(index))
#     y_vals.append(random.randint(-5,5))
    
#     plt.cla() # to stop the disco color try it commenting this and then run 
#     plt.plot(x_vals, y_vals)
#     # plt.axhline(0, color='red', label='Median_age', linewidth=2)


# ani = FuncAnimation(plt.gcf(), animate, interval=1000) #gcf = get current figure and 1000 means 1second

# plt.tight_layout()
# plt.show()




import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

index = count()


def animate(i):
    data = pd.read_csv('datata.csv')
    x = data['x_value']
    y1 = data['total_1']
    y2 = data['total_2']

    plt.cla()

    plt.plot(x, y1, label='Channel 1')
    plt.plot(x, y2, label='Channel 2')

    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()