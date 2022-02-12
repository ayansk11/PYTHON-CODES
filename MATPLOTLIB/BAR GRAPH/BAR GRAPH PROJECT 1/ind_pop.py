import csv
import os
from matplotlib import pyplot as plt
import numpy as np

def bar_graph():

    years = []
    total = []
    rural = []
    urban = []

    if os.path.exists("pop.csv"):

        with open("pop.csv", 'r') as file:
            read = csv.reader(file)
            read_list = list(read)

            for f in read_list[1:]:
                years.append(int(f[0]))
                total.append(int(f[1]))
                rural.append(int(f[2]))
                urban.append(int(f[3]))

            plt.style.use("fivethirtyeight")

            plt.figure(figsize=(12,8))

            plt.xlabel("YEAR")
            plt.ylabel("POPULATION IN BILLIONS")
            plt.title("---- INDIAN POPULATION CENCUS 2001* ----")
            plt.xticks(ticks=np.arange(1901, 2002, 10))

            plt.bar(years, total, width=5, edgecolor="white", linewidth=0.7, label = "total")
            plt.bar(years, rural, width=5, edgecolor="white", linewidth=0.7, label = "rural")
            plt.bar(years, urban, width=5, edgecolor="white", linewidth=0.7, label = "urban")
           
            plt.grid(True, color='k', linestyle=':')
            plt.tight_layout()

            plt.legend()
            plt.show()

bar_graph()
  