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

            fig, ax = plt.subplots()

            plt.xlabel("YEAR")
            plt.ylabel("POPULATION IN BILLIONS")
            plt.title("---- POPULATION CENCUS 2001* ----")

            plt.bar(years, total, width=5, color="r", edgecolor="white", linewidth=0.7, label = "total")
            plt.bar(years, rural, width=5, color="y", edgecolor="white", linewidth=0.7, label = "rural")
            plt.bar(years, urban, width=5, color="b", edgecolor="white", linewidth=0.7, label = "urban")
            ax.set(xticks=np.arange(1901, 2002, 10), yticks = total)

            plt.legend()
            plt.show()

bar_graph()
  