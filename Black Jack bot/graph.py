import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use("fivethirtyeight")


def animate(i):
    data = pd.read_csv("Black Jack bot\output.csv")
    x = data["x_value"]
    y1 = data["balance"]

    plt.cla()

    plt.plot(x, y1, label="Balance")
    # plt.plot(x, y2, label="Channel 2")

    plt.legend(loc="upper left")
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=100)

plt.tight_layout()
plt.show()

