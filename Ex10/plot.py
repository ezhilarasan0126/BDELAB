import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Step 2: Simulate sample Big Data summary (e.g., sales per month)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [1500, 1800, 2200, 2400, 2000, 2700]

df = pd.DataFrame({'Month': months, 'Sales': sales})

# Line Chart - Sales trend
plt.figure(figsize=(6, 4))
plt.plot(df['Month'], df['Sales'], marker='o', linestyle='-', color='green')
plt.title("Monthly Sales Trend (Big Data Sample)")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

# Bar Chart - Sales per month
plt.figure(figsize=(6, 4))
sns.barplot(x='Month', y='Sales', data=df, palette='crest')
plt.title("Bar Chart of Sales per Month")
plt.show()

# Pie Chart - Sales proportion per month
plt.figure(figsize=(5, 5))
plt.pie(df['Sales'], labels=df['Month'], autopct='%1.1f%%', startangle=90, colors=sns.color_palette("pastel"))
plt.title("Sales Distribution")
plt.axis('equal')
plt.show()
