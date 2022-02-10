import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("sats.csv")

year = data["year"]
total = data["total"]
male = data["male"]
female = data["female"]

x_index = np.arange(2010, 2021)

plt.style.use("fivethirtyeight")

plt.figure(figsize=(10, 6), dpi=80)
plt.xticks(ticks=x_index)

plt.plot(x_index, total, marker="o", label="Total Student")
plt.plot(x_index, male, marker="o", label="Male Student")
plt.plot(x_index, female, marker="o", label="Female Student")

plt.title("Students taking SAT Exam by year")
plt.xlabel("Year")
plt.ylabel("Number of Students")

plt.grid(True, color='k', linestyle=':')
plt.tight_layout()
plt.legend()

plt.show()
