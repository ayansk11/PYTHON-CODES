import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("sats.csv")

year = data["year"]
total = data["total"]
male = data["male"]
female = data["female"]

x_index = np.arange(2010, 2021)
width = 0.3

plt.style.use("fivethirtyeight")

plt.figure(figsize=(10, 6), dpi=80)
plt.xticks(ticks=x_index)

plt.bar(x_index-width, total, width=width, label="Total Students")
plt.bar(x_index, male, width=width, label="Male Students")
plt.bar(x_index+width, female,width=width, label="Female Students")

plt.title("Students taking SAT Exam by year")
plt.xlabel("Year")
plt.ylabel("Number of Students")

plt.grid(True, color='k', linestyle=':')
plt.tight_layout()
plt.legend()

plt.show()